# IOC ( Inversion Of Control )

*  IOC 컨테이너는 Inversion of Control(제어의 역전)의 약어인 디자인 패턴이다.
   *  컨테이너 : 객체의 생명주기를 관리, 생성된 인스턴스들에게 추가적인 기능을 제공하게 하는 것
> 객체의 생성, 생명주기의 관리까지 모든 객체에 대한 제어권이 바뀌었다는 것을 의미한다.

> 쉽게 말하면 "니가 해"

코드로 간단한 예를 들어보자.

```java
public class A{
    
    private B b;

    public A(){
        b = new B();
    }
}
```

A객체는 B객체를 의존하고 있다. 즉 **제어를 개발자**가 관리한다.

```java
public class A{

    @Autowired
    private B b;

}
```

B 객체가 스프링 컨테이너에 의해 관리되고 있다면 `@Autowired`를 통해 객체를 주입받을 수 있게 된다.

이것은 스프링 컨테이너에서 직접 객체를 생성하여 해당 객체로 주입 시켜준 것이다.

이것이 바로 제어의 역전이다.
`
### 장점

* POJO의 생성, 초기화, 서비스 소멸에 관한 권한을 갖음
  * POJO(Plain Old Java Object) : 특정 자바 모델이나 기능, 프레임워크를 따르지 않는 Java Object를 말한다.
  * ex) Java Bean 객체, getter, setter
* TDD에 용이
* 개발자는 비지니스 로직에 집중 가능

### Spring에서의 IoC

스프링 프레임워크의 장점으로 IoC 컨테이너 기능이 있다. 그러나 스프링 프레임워크가 생기기 전부터 IoC 컨테이너는 사용되던 개념이였다. 

그래서 스프링 프레임워크만의 장점이 아니라는 반론이 나오게 됐고, DI라는 용어가 나오게 됐다.

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fc3pCjO%2FbtqCbUccN0s%2FVSRbh2Kdvm3lakFBVBOaI0%2Fimg.png)

> DL 사용시 컨테이너 종속이 증가하기 때문에 주로 DI를 사용함

### Dependency Lookup

* 저장소에 저장되어 있는 Bean에 접근하기 위해 컨테이너가 제공하는 API를 이용하여 Bean을 Lockup하는 것

### Dependency Injection

* 각 클래스간의 의존관계를 빈 설정(Bean Definition) 정보를 바탕으로 컨테이너가 자동으로 연결해주는 것
  * Setter Injection (수정자 주입)
    * ```java
        @ResController
        public class Controller {
            private Service service;

            @Autowired
            public void setService(Service service){
                this.service = service;
            }
        }
  * Field Injection (필드 주입)
    * ```java
        @RestController
        public class Controller {
            @Autowired
            private Service service;
        }
        ```
  * Constructor Injection (생성자 주입)
    * ```java
        @RestController
        public class Controller {
            private final Service service;

            public Controller(Service service){
                this.service = service;
            }
        }
        ```
        > 생성자 주입을 사용하는게 좋다.


## BeanFactory, ApplicationContext

### BeanFactory

* BeanFactory 계열의 인터페이스만 구현한 클래스는 단순히 컨테이너에서 객체를 생성하고 DI를 처리하는 기능만 제공한다.
* Bean 등록, 생성, 반환 관리를 한다.
* 컨테이너가 구동될 때 Bean 객체를 생성하는 것이 아니라 클라이언트의 요청에 의해서 Bean 객체가 사용되는 시점(Lazy Loading)에 객체를 생성하는 방식이다.
* 빈을 조회할 수 있는 `getBean()` 메서드가 정의되어 있다.
  * `getBean()`이 호출되면 팩토리는 의존성 주입을 이용해 빈을 인스턴스 화하고 빈의 특성을 설정하기 시작. 여기서 빈의 일생이 시작된다.
> 잘 사용하지 않음

### ApplicationContext

* BeanFactory를 상속받은 인터페이스이다.
  * 그렇기에 역시 Bean 객체를 생성, 관리한다.
* BeanFactory와 달리 컨테이너가 구동되는 시점(Pre Loading)에 객체를 생성하는 방식이다.
> 많이 사용한다.

#### BeanFactory보다 추가적으로 제공하는 기능

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FnsE6w%2Fbtq9flCz2G4%2FumjyApnZqSkHTQZ4Aa1f60%2Fimg.png)

* 국제화가 지원되는 텍스트 메시지를 관리 해준다.
* 이미지같은 파일 자원을 로드할 수 있는 포괄적인 방법을 제공해준다.
* 리스너로 등록된 빈에게 이벤트 발생을 알려준다.