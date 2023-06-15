# **Checked Exception 과 Unchecked Exception**

자바의 예외는 크게 3가지로 나눌 수 있습니다.
+ 체크 예외(Checked Exception)
+ 에러(Error)
+ 언체크 예외(Unchecked Exception)

![img](https://user-images.githubusercontent.com/45676906/105691109-2cda9400-5f40-11eb-9003-a14873c2eaf2.png)

자바에서 에러, 예외 관련된 클래스들의 계층구조는 위와 같습니다. Throwable 클래스를 기준으로 Error, Exception 클래스로 나뉘어집니다. 왼쪽에 보이는 Error는 말 그대로 에러와 관련된 클래스입니다. 그리고 오른쪽에 보이는 Exception도 말 그대로 예외와 관련된 클래스 입니다. 자바에서는 실행 시(runtime) 발생할 수 있는 프로그램 오류를 에러(error)와 예외(exception) 두 가지로 구분하였습니다.

<br>

## **에러(Error)란?**

에러는 시스템에 비정상적인 상황이 발생했을 경우에 발생합니다. 예를들어, 메모리 부족(OutofMemoryError)이나 스택오버플로우(StackOverflowError)와 같이 복구할 수 없는 것을 말합니다. 이러한 에러는 개발자가 예측하기도 쉽지 않고 처리할 수 있는 방법도 없습니다.

<br>

## **예외(Exception)란?**

예외는 프로그램 실행 중에 개발자의 실수로 예기치 않은 상황이 발생하였을 때 입니다. 예를들어 배열의 범위를 벗어난(ArrayIndexOutOfBoundsException), 값이 null인 참조변수를 참조(NullPointerException), 존재하지 않는 파일의 이름을 입력(FileNotFoundException) 등등이 있습니다. 이러한 것들은 그냥 보아도 프로그램에 심각한 오류여서 복구할 수 없는 수준은 아니라는 것을 알 수 있습니다.   
예외에는 2가지로 나눌 수 있습니다.

+ 체크 예외(Checked Exception)
+ 언체크 예외(Unchecked Exception)

위의 자바 에러 클래스의 계층 구조를 보았을 때 RuntimeException의 하위 클래스들이 Unchecked Exception이라 하고 RuntimeException의 하위 클래스가 아닌 Exception 클래스의 하위 클래스들을 Checked Exception이라고 한다.

<br>

## **체크 예외(Checked Exception)**

체크 예외는 RuntimeException의 하위 클래스가 아니면서 Exception 클래스의 하위 클래스들입니다. 체크 예외의 특징은 반드시 에러 처리를 해야하는 특징(try/catch or throw)을 가지고 있습니다.

+ 존재하지 않는 파일의 이름을 입력(FileNotFoundException)
+ 실수로 클래스의 이름을 잘못 적음(ClassNotFoundException)

체크 예외의 예시는 이러한 것들이 있습니다.

<br>

## **언체크 예외(Unchecked Exception)**

언체크 예외는 RuntimeException의 하위 클래스들을 의미합니다. 이것은 체크 예외와는 달리 에러 처리를 강제 하지 않습니다.
말 그대로 실행 중에(runtime) 발생할 수 있는 예외를 의미합니다.

+ 배열의 범위를 벗어난(ArrayIndexOutOfBoundsException)
+ 값이 null이 참조변수를 참조(NullPointerException)

언체크 예외는 이러한 것들이 있습니다.   

만약 언체크 예외가 에러 처리를 강제해야 했다면 아래와 같은 상황이 발생할 것입니다.

```java
public class ArrayTest {
    public static void main(String[] args) {
        try {
            int[] list = {1, 2, 3, 4, 5};
            System.out.println(list[0]);
        } catch (ArrayIndexOutOfBoundsException e) {
            e.printStackTrace();
        }
    }
}
```

단순히 배열을 만들어 배열의 원소를 출력하고자 하는데 try/catch문을 꼭 사용해야 합니다. 이러한 RuntimeException은 개발자들에 의해 실수로 발생하는 것들이기 때문에 에러를 강제하지 않는 것입니다.

> 컴파일러가 에러처리를 확인하지 않는 RuntimeException 클래스들은 unchecked 예외라고 부르고 예외처리를 확인하는 Exception 클래스들은 checked 예외라고 부릅니다.

<br>

## **체크 예외와 언체크 예외의 Rollback 여부**

| |Checked Exception|Unchecked Exception|
|--|--|--|
|처리여부|반드시 예외를 처리해야 함|명시적인 처리를 강제하지 않음|
|확인시점|컴파일 단계|실행단계|
|예외발생시 트랜잭션 처리|roll-back 하지 않음|roll-back 함|
|대표 예외|Exception의 상속받는 하위 클래스 중 RuntimeException을 제외한 모든 예외   (IOException, SQLException)|RuntimeException 하위 예외 (NullPointerException, IllegalArgumentException, IndexOutOfBoundException, SystemException)|

체크 예외와 언체크 예외의 차이점 중에 같이 보아야 할 점은 Rollback의 여부입니다.

+ 체크 예외 : Rollback이 되지 않고 트랜잭션이 commit까지 완료됩니다.
+ 언체크 예외 : Rollback이 됩니다.

<br>

## **Checked Exception vs Unchecked Exception 선택하기**

+ 임의의 예외 클래스를 만들어 예외 처리를 하는 경우가 많을 것인데 이 때 try-catch로 묶어줄 필요가 있을 경우에만 Exception 클래스를 확장한다.
+ 일반적으로 실행시 예외를 처리할 수 있는 경우에는 RuntimeException 클래스를 확장해 Unchecked Exception을 사용하는 것이 좋다.
