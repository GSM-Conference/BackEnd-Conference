# **Bean 이란?**
Bean이란 스프링(Spring) IoC 컨테이너가 관리하는 자바 객체를 빈(Bean)이라 한다.

<br><br>

# **Bean을 등록하는 방법**

<br>

## **1. 어노테이션(Annotation)을 사용하는 방법**
Bean을 등록하기 위해서는 **@Component** Annotation을 사용한다. @Component가 등록되어 있는 경우에는 스프링이 확인하여 빈으로 등록시킨다.   

직접 @Component를 작성하여도 되고, **스테레오 타입(sterotype)인 @Controller, @Service, @Repository**와 같은 어노테이션들도 자동으로 스캔하여 빈에 등록된다.   

@Controller 어노테이션을 타고 들어가 보면 다음과 같이 나타난다.
![controller](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcXLjRP%2FbtrK9zcfZwW%2F4ksVYnymsNnWSpMhyq2JXk%2Fimg.png)   
이와 같이 컨트롤러 어노테이션 안에 @Component가 존재하여 이러한 현상이 일어나는 것이다.

<br>

## **2. 빈 설정 파일에 직접 등록하는 방법**
해당 방법은 **@Configuration**과 **@Bean** 어노테이션을 사용한다.   
@Configuration 어노테이션의 경우 간단하게 말하면 **해당 파일에 빈을 등록할 것이니 조회해라**라는 것이다.   
@Configuration 어노테이션이 붙은 파일 내에서 @Bean 어노테이션을 사용해서 빈을 직접 등록하는데, @Bean을 사용해 수동으로 등록할 때에는 해당 메서드 이름이 빈 이름으로 결정된다.
### 예시
```java
@Configuration
public class MozziConfig {

    @Bean
    public FilterRegistrationBean logFilter(){
    
    }
```

<br>

# **마무리**
**스프링의 경우 @Component 스캔을 통해 자동으로 빈 등록을 하는 방식을 권장한다.**   
Spring에서는 Main App 클래스에서 @ComponentScan 어노테이션을 사용해서 등록해야 하며   
Springboot 환경에서는 디폴트로 존재하는 @SpringBootAplication에 @ComponentScan 어노테이션이 포함되어있다.
![springbootaplication](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbAHFXy%2FbtrK7DzlASQ%2FrkTLmaZUQhKdAL9QmKdI11%2Fimg.png)


