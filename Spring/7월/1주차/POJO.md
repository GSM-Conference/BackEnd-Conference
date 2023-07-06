# POJO 란?

* POJO란 Plain Old Java Object의 약어로 순수하게 자바로만 이루어진 객체를 말한다.

```java
public class User {
    private final int id;
    private final String name;
    private final String email;
    
    public int getId() {
    	return id;
    }
    public String getName() {
    	return name;
    }
    public String getEmail() {
    	return email;
    }
    
    public void setId(int id) {
    	this.id = id;
    }
    public void setName(String name) {
    	this.name = name;
    }
    public void setEmail(String email) {
    	this.email = email;
    }
}
```

위처럼 getter/setter 와 같은 기본적인 자바 기능을 갖는 객체를 POJO라고 한다.

> getter/setter를 가지고 있는 객체만이 POJO인 것이 아니고 POJO에 포함되는 것이다.

> ORM을 사용하고 싶다면 ORM을 지원하는 ORM 프레임워크를 사용해야 한다. Hibernate 를 사용한다고 가정해보자. 만약 자바 객체가 ORM을 사용하기 위해 Hibernate를 직접 의존하는 순간 그건 POJO가 아니게 된다. 특정 `기술`에 의존하고 있기 때문이다.

## 그럼 특정 기술을 어떻게 사용해?

그래서 Hibernate를 어떻게 사용하나? 특정 기술에 종속하면 POJO가 아니라고 했으면서 Spring에서는 어떻게 사용할까? 그건 바로 스프링에서 정한 표준 인터페이스가 있기 때문이다. 스프링 개발자들은 ORM이라는 기술을 사용하기 위해 `JPA`라는 표준 인터페이스를 지정했다. 그리고 이제 여러 ORM 프레임워크들은 JPA를 구현하여 실행된다. 이것을 `PSA` 라고 한다.

## POJO를 지향해야 하는 이유

스프링 프레임워크가 나오기 전에는 원하는 엔터프라이즈 기술이 있으면 그 기술을 직접적으로 사용하는 객체를 설계했다. 특정 기술에 종속하게 된 자바 코드는 가독성이 떨어지고 유지보수에 어려움이 생겼다. 또한 특정 기술의 클래스를 상속 받거나, 직접 의존하게 되어 확장성이 떨어지는 단점이 있다. 즉 자바가 객체지향의 장점을 잃게 된것이다. 그래서 POJO를 지향해야 한다.