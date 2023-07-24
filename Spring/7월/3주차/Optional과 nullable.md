## **Nullable vs Optional**
자바에서는 Optional을 사용하여 객체가 null일 경우 예측하지 못한 곳에서 발생할 수 있는 NullPointException(NPE)을 통제한다.

Optional은 해당 객체가 null일 수도 있고 아닐 수도 있다는걸 의미한다.

코틀린은 아래와 같이 변수 선언시 해당 변수가 null이 가능한지 불가능한지를 설정을 한다.

```kt
// val : 변경 불가능한 변수, 자바의 final 개념
// var : 변경 가능한 변수

// Non-Null (null 할당 불가능)
val title: String
var contents: String

// Nullable (null 할당 가능)
val title: String?
var contents: String?
```
기본적으로 코틀린 변수는 null을 할당할 수 없다.
하지만 null을 사용해야 할 경우는 변수의 타입 뒤에 ? 를 붙여서 null이 할당 될 수 있음을 표현해준다.

### **코틀린 let() vs 자바 Optional map()**
자바 Optional을 쓰면 가장 많이 쓰게 되는 map() 메소드이다.   

코틀린에는 자바의 map()과 비슷한 동작을 하는 let()이라는 메소드가 있다.

#### **자바 Optional map()**
```java
// 자바 Optional의 map()을 사용하는 경우
BoardDto boardDto = boardRepository.findById(boardId)
        .map(board -> {
            return new BoardDto(board);
        })
        .orElse(new Board());
```

#### **코틀린 let()**
```kt
// 코틀린의 let()을 사용하는 경우 - 람다식 사용
var boardDto = boardRepository.findByIdOrNull(boardId)
    ?.let { board ->
        BoardDto(board)
    }

// 코틀린의 let()을 사용하는 경우 - it 사용 : it라는 키워드가 위 람다식에서 본 board와 동일한 값이다.
var boardDto = boardRepository.findByIdOrNull(boardId)
    ?.let {
        BoardDto(it)
    }
```
자바 Optional의 map() 에는 Optional이 감싸고 있는 값이 null이 아닐 경우에 실행되는 로직을 작성하는데 코틀린에서도 마찬가지로 null이 아닐경우에 실행하는 부분이 필요하다.

null일 때도 실행이 되면 결국 NPE를 피하기 위해 null 체크를 해줘야 하기 때문이다.

그래서 코틀린에는 ?.라는 Safe-Call Operator가 존재한다.

?.는 null이 아닐경우 뒷 부분 수행이라고 한 문장으로 풀어서 설명할 수 있다.

그리고 let() 메소드는 위 코드처럼 두 가지 방식으로 작성이 가능한데 let() 안에있는 람다식 부분의 파라미터는 it라는 키워드로 대체가 가능하다.

let() 메소드의 또 다른 특징으로 return 키워드를 사용하지 않아도 let() 안에 작성된 코드 중 가장 마지막 라인이 최종 리턴값이 된다.

따라서 위 코틀린 코드는 findByIdOrNull() 을 통해 조회된 값 혹은 null이 넘어올 수 있는데 null이 아닌 경우에만 BoardDto를 리턴하라는 의미로 이해할 수 있다.

### **코틀린 엘비스 연산자 vs 자바 Optional orElse()**
엘비스 연산자란 ?: 모양으로 생긴 연산자를 말한다. 이 엘비스 연산자는 null일 경우 뒷 부분 수행이라고 생각하면 된다. 자바의 orElse()와 같은 역할이다.

#### **자바 Optional orElse()**
```java
// orElse() - null일 경우 Board 객체 반환
BoardDto boardDto = boardRepository.findById(boardId)
        .map(board -> {
            return new BoardDto(board);
        })
        .orElse(new Board());

// orElseGet() - null일 경우 메소드 수행
BoardDto boardDto = boardRepository.findById(boardId)
        .map(board -> {
            return new BoardDto(board);
        })
        .orElseGet(() -> getDefaultBoard());

// orElseThrow() - null일 경우 예외 발생
BoardDto boardDto = boardRepository.findById(boardId)
        .map(board -> {
            return new BoardDto(board);
        })
        .orElseThrow(() -> new NotFoundException())
```

#### **코틀린 엘비스 연산자**
```kt
// null일 경우 Board 객체 반환, orElse()와 동일
var boardDto = boardRepository.findByIdOrNull(boardId)
    ?.let {
        BoardDto(it)
    }
    ?: Board()

// null일 경우 메소드 수행, orElseGet()과 동일
var boardDto = boardRepository.findByIdOrNull(boardId)
    ?.let {
        BoardDto(it)
    }
    ?: getDefaultBoard()

// null일 경우 예외 발생, orElseThrow()와 동일
var boardDto = boardRepository.findByIdOrNull(boardId)
    ?.let {
        BoardDto(it)
    }
    ?: throw NotFoundException("$boardId Not Found")
```

### **코틀린 !! 연산자 vs 자바 Optional get()**
자바에서는 Optional이 감싸고 있는 값이 확실히 null이 아니라면 get()을 통해 값을 반환받을 수 있다.

코틀린에서는 !! 연산자가 같은 역할을 한다.

#### **자바 Optional get()**
```java
Optional<String> text = Optional.of("not null string");
boolean isLegalLength = text.get().length() > 5;
```

#### **코틀린 !! 연산자**
```kt
val text: String = "not null string"
var isLegalLength = text!!.length > 5
```
위와 같이 코틀린에서는 !! 을 사용하여 값이 null이 아님을 단언할 수 있다.

### **결론**
코틀린은 Nullable 타입의 처리를 단순화하는 다양한 기본 제공 연산자와 표준 라이브러리 함수를 제공한다. 이것들을 사용하면 짧고, 간결하며, 읽기 쉬운 코드를 작성할 수 있다. 특히 매우 긴 연결코드에서 사용할 경우 더욱 유용하다.

읽기 쉬운 코드를 작성할 수 있는 장점 이외에도 코틀린의 Nullable 타입에는 자바의 Optional 타입과 다른 다음의 장점들이 있다.

첫째, Optional이 안전한 null 처리를 위해 값을 wrapping하는 wrapper 객체를 추가로 만드는 것과 달리, 코틀린은 null 처리만을 위한 wrapper 객체를 따로 만들지 않기 때문에 런타임 시에 추가적인 오버 헤드가 발생하지 않는다.

둘째, 코틀린의 Nullable 타입은 컴파일 타임에 널 안정성을 제공한다. 만약 안전하지 않은 방법으로 사용하면 컴파일 타임 오류가 발생한다. 반면, Optional 타입을 안전하지 않은 방법으로 사용한다고 하더라도 컴파일러는 검사하지 않으며 이 경우 런타임 시에 예외가 발생할 수 있다.