# JVM
> Java Virtual Machine 의 줄임말 이며 Java Byte Code를 OS에 맞게 해석 해주는 역할을 합니다.



### 자바 코드 실행 과정

자바 코드는 아래와 같은 순서로 동작한다.

![img](https://velog.velcdn.com/images/soyeon207/post/e6946856-4ab7-4ce7-9e44-d5de75544d46/image.png)

1. 자바 소스 코드(.java)를 작성한다.
2. 컴파일러(Javac.exe)에서 자바 코드를 바이트코드(.class)로 변환한다.
3. 런처(java.exe)로 JVM을 가동시킨다.

Java compiler는 .java라는 파일을 .class라는 Java Byte Code로 변환시켜줍니다. Byte Code는 기계어가 아니기 때문에 OS에서 바로 실행되지 않습니다. 이때 JVM이 OS가 Byte Code를 이해할 수 있도록 변환시켜주는 역할을 합니다.

> .java 파일이란 ?
>
> + java 규칙에 맞게 작성한 모든 소스코드 파일<br>
> + 사람이 읽을 수 있는 text 로 구성


> .class 파일이란 ?
>
> + 컴파일러에 의해 생성된 바이트코드로 형성된 파일<br>
> + JVM을 위한 코드
> + 자바를 실행할 수 있는 모든 장치에서 실행 가능

### JVM 구동방식

![img](https://user-images.githubusercontent.com/39696812/144742938-19b542bf-407b-43cf-8d9e-824c93583cc9.jpg)

큰 단위로 봤을때 JVM은 3가지로 나눌 수 있다.

### 클래스 로더 (Class Loader)
>클래스 로더는 .class파일을 동적으로 로드하고, 해당 바이트 코드들을 Runtime Data Area에 배치한다.

동적으로 로드한다는 건 한번에 메모리에 올리지 않고, 어플리케이션에 필요한 경우에만 동적으로 메모리에 적재한다는 뜻입니다.

클래스 로더의 로딩 순서는 `Loading -> Linking -> Initialization` 순서로 이뤄진다.

![img](https://user-images.githubusercontent.com/39696812/145208079-928a85d2-0cd2-4bca-854c-9cb1cdea6afb.png)

#### 1. Loading
.class 파일을 읽고 그 코드에 따라 적절한 바이너리 데이터를 만든 다음 메소드 영역에 저장한다.

#### 2. Linking
클래스 파일을 사용하기 위해 검증하는 과정이다.

#### 3. Intialization
링크 단계의 prepare에서 확보한 메모리 영역의 클래스의 static 값들을 할당한다.

### Runtime Data Area
>Runtime Data Area는 쉽게 메모리 영역이라고 생각하면 된다.
애플리케이션을 실행할 때 사용되는 데이터들을 적재하는 영역이다.

![img](https://user-images.githubusercontent.com/39696812/145206269-5788893b-f066-40a7-b0ce-6a7a2baf64dc.png)

위 그림처럼 Method / Heap / PC Register / Stack / Native Method Stack 으로 나눌 수 있다.

Method Area와 Heap Area는 모든 스레드에서 사용되고, PC Register, Stack, Native Method Stack은 각 스레드별로 생성된다.

### 실행 엔진 (Execution)
>실행 엔진은 클래스 로더를 통해 Runtime Data Area에 배치된 바이트 코드를 명령어 단위로 읽어서 실행한다. 클래스를 실행시키는 역할이다.

인터프리터와 JIT 컴파일러 방식을 혼합해서 바이트 코드를 실행한다.

#### 1. 인터프리터
자바 바이트 코드를 명령어 단위로 하나하나씩 읽어서 바로 해석하고 실행한다.<br>
JVM 안에서 바이트코드는 기본적으로 인터프리터 방식으로 작동한다.

#### 2. JIT 컴파일러
인터프리터 효율을 높이기 위해 인터프리터가 반복되는 코드를 발견하면 JIT컴파일러로 반복되는 코드를 모두 Native Code로 바꾼다.
그렇게 되면 반복된 Byte Code는 Native Code로 바뀌어 있기 때문에 인터프리터가 바로 사용할 수 있게 된다.

### 가비지 콜렉터
RuntimeDateArea의 Heap 영역의 더 이상 사용하지 않는 메모리를 찾아서 삭제한다.
