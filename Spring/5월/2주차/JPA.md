## JPA란?

JPA는 Java Persistence API의 약자로 자바 ORM 기술에 대한 API 표준 명세를 뜻한다. 대표적으로 패러다임 불일치 문제를 해결해주고, 영속성 컨텍스트를 제공해준다.

> ORM 이란?
Object Relational Mappaing의 약자로 객체와 관계형 데이터 베이스를 매핑해주는 기술이다. 객체는 객체대로, 관계형 데이터베이스는 관계형 데이터베이스대로 설계하고, ORM 프레임 워크가 중간에서 매칭을 해주는 역할을 한다.


JPA는 인터페이스의 모음이다. 단순한 명세이기 때문에 구현체가 없다. 근데 우리는 어떻게 JPA라는걸 사용할 수 있을까?

## Hibernate

![](https://velog.velcdn.com/images/sunggil-5125/post/2c763db0-cd8b-4909-8b6d-3a0c4e04c45e/image.png)

우리는 Hibernate가 JPA를 구현한 구현체이기 때문에 JPA를 쓸 수 있는것이다!
개발한지 10년이 넘었고, 대중적으로 많이 이용하는 유명한 JPA의 구현체 중 하나이다.
Hibernamte는 내부적으로 JDBC를 이용해 관계형 데이터베이스와 커넥션을 맺고 상호작용한다.

JPA를 구현하는 다른 구현체들로는 EclipseLink나 DataNuclenus 등이 있다고 한다.

만약 JPA를 구현하는 구현체들이 프로젝트에서 맞지 않거나 마음에 들지 않는 경우 개발자가 직접 JPA 구현체를 만들어 사용할 수 있다고 한다.

## 영속성 컨텍스트

JPA가 뭔지 알았으니 JPA의 내부 구조가 어떻게 돌아가는지 알아보자. 그러기 위해서는 영속성 구조에 대해서 이해해야 한다.

애플리케이션을 개발하면 EntityManagerFactory를 통해서 클라이언트 요청이 들어올때 마다 EntityManager를 생성한다. 또 EntityManager를 통해서 내부적으로 DB 커넥션을 해 DB를 사용하게 되는것이다.

![](https://velog.velcdn.com/images/sunggil-5125/post/8c9415ee-369c-4914-92db-8dc08b738df8/image.png)

위에 사진을 통해서 persist() 메서드가 어떻게 돌아가는지 알아보자.

#### 1. 개발자가 userRepository.save(userA) 요청을 한다.

개발자가 Entity를 DB에 저장하기 위해서 save 요청을 하면 EntityManager를 통해 persist()를 호출하게 된다. 

```java
SimpleJpaRepository.java

/*
 * (non-Javadoc)
 * @see org.springframework.data.repository.CrudRepository#save(java.lang.Object)
 */
@Transactional
@Override
public <S extends T> S save(S entity) {

	if (entityInformation.isNew(entity)) {
		em.persist(entity);
		return entity;
	} else {
		return em.merge(entity);
	}
}
```

왜냐하면 위에 ```save()``` 메서드를 까보면 새로운 entity라면 ```persist()``` 메서드를 호출하게 개발이 되어 있기 때문이다. 새로운 entity가 아니라면 ```merge()``` 메서드를 호출하는데 ```merge()``` 메서드는 말그대로 병합 해주는 역할을 한다.

#### 2. 영속성 컨텍스트 진입

```persist()``` 호출시 userA라는 객체는 영속성 컨텍스트 영역에 진입하게 된다. 이 영역에 진입시 Entity 단위로 변환되어 진입한다. 이렇게 영속성 컨텍스트 영역에 진입한 entity는 key-value로 1차 캐시 라는 영역에 또 저장된다. 이때 key는 @Id 어노테이션이 붙은 필드이고, value는 entity로 저장된다.
또한 동시에 userA entity를 DB에 저장하기 위한 insert 쿼리가 쓰기지연 SQL 저장소에 저장된다.

#### 3. 트랜젝션 커밋시 쿼리문 DB에 전송

JPA는 한 트랜잭션 단위를 기반으로 DB에 작업을 처리한다. 트랜잭션 단위에 있는 비지니스 로직을 모두 처리한 후 commit() 메서드를 호출하면 쓰기지연 SQL 저장소에 저장되었었던 모든 쿼리문이 DB에 날라간다.
일차적으로는 그렇게 보일 수도 있지만 commit() 메서드가 flush() 메서드를 호출해 쿼리문이 DB에 날라가는것이다.

---

## Entity의 생명주기

Entity의 생명주기는 4가지로 나뉜다.

>
- 영속 상태
- 비영속 상태
- 준영속 상태
- 삭제 상태

``` java
User user = new User();
user.setId(1L);
user.setName("JPA!"); // 여기까지는 비영속 상태

em.persist(user); // 영속 상태 (영속성 컨텍스트에 의해 관리된다)
// => But, 아직 DB 에 저장되진 않았다. 즉 SQL 쿼리가 아직 안날라감

em.detach(user); // 준영속 상태
// => user 를 영속성 컨텍스트에서 분리한다. Dirty Checking.. 등 기능들을 사용하지 못함

em.remove(user); // 실제 DB에 영구 저장된 상태인 user 객체를 지우겠다는 요청
```
---

## 변경 감지(Dirty Checking)

JPA는 수정과 관련된 메소드가 존재하지 않는다. 변경감지는 데이터를 수정 할 수 있게 해주는 기능으로써, 
트랜잭션 커밋시 영속화된 entity에서 가지고 있던 스냅샷(최소 정보)와 바뀐 entity 정보를 비교해서 바뀐 부분을 수정 해주는 기능이다. 

```java
memberA.setNamge(10); // 영속 Entity 데이터 수정
// => 더티 체킹으로 인해, persist() 를 호출하지 않아도 자동으로 데이터가 수정된다.

transaction.commit(); // 트랜잭션 커밋
```
위 코드 처럼 데이터가 바뀌면 스냅샷과 비교해 바뀌면 update 쿼리를 날린다.