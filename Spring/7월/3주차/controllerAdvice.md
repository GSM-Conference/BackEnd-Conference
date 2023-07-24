# @ControllerAdvice 란?

## Spring에서 Exception을 Catch하는 과정

```java
@Controller
public class SimpleController {

    // ...

    @ExceptionHandler(value = RuntimeException.class)
    public ResponseEntity<String> handle(IOException ex) {
        // ...
    }
    
    public ResponseEntity<String> noHandler(IOException ex) {
        // ...
    }
}
```

* `@ExceptionHandler`는 `@Controller`에서 발생하는 예외를 잡아 메서드에서 처리한다.
> 그러나 만약 `@ExceptionHandler`가 정의되어 있지 않은 다른 메서드에서 `RuntimeException`이 터진다면 잡지 못한다. 즉 컨트롤러마다 `@ExceptionHandler`를 정의해주어야 한다.

그래서 우리는 `@ControllerAdvice`를 사용한다. `@ControllerAdvice`는 `@Controller` 어노테이션이 적용된 모든 곳에서 발생하는 예외를 catch 한다.

```java
@Slf4j
@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(TestException.class)
    public ResponseEntity<ErrorMessage> globalExceptionHandler(TestException e) {
        printError(e, e.getErrorCode().getMessage());
        return new ResponseEntity<>(new ErrorMessage(e.getErrorCode()), HttpStatus.valueOf(e.getErrorCode().getStatus()));
    }

    private void printError(RuntimeException e, String message) {
        log.error(message);
        e.printStackTrace();
    }
}
```

## ControllerAdvice, RestControllerAdvice

### ControllerAdvice

> RestControllerAdvice는 그냥 `@ResponseBody` + `ControllerAdvice` 이다.

`@ControllerAdvice` 어노테이션은 `@ExceptionHandler`, `@ModelAttribute`, `@InitBinder` 가 적용된 메서드들에 AOP를 적용해 `Controller` 단에 적용하기 위해 고안된 어노테이션이다.

> 근데 사실 AOP로 구현되지 않았다고 한다. 그냥 `ControllerAdvice`의 동작 방식이 `Controller`에 AOP를 적용하는 느낌이라고 한다.

클래스에서만 선언하면 되고, 모든 `Controller`에 대해 전역적으로 발생할 수 있는 예외를 잡아서 처리한다. 

`@Component`가 선언되어 있어 빈으로 관리되어 사용됩니다.



## ExceptionHandler

> 실질적으로 예외를 처리하는 어노테이션

`@ExceptionHandler` 어노테이션을 메서드에 선언하고 특정 예외 클래스를 지정해주면 그 예외가 발생했을 때 메서드에 정의한 로직을 처리를 할 수 있다.

```java
@ExceptionHandler(TestException.class)
public ResponseEntity<ErrorMessage> globalExceptionHandler(TestException e) {
    printError(e, e.getErrorCode().getMessage());
    return new ResponseEntity<>(new ErrorMessage(e.getErrorCode()), HttpStatus.valueOf(e.getErrorCode().getStatus()));
}
```

즉, 내가 처리하고 싶은 Exception을 정의하고 그 예외가 발생 시 내가 원하는대로 처리할 수 있다는 것이다.