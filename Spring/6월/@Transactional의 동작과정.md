## @Transaction의 동작 과정
@Transactional 어노테이션은 Spring AOP를 기반으로 동작한다.
AOP에 대해서 먼저 알아보자!

## 💻 AOP란?

![](https://velog.velcdn.com/images/sunggil-5125/post/d546905b-aa99-4b70-aa26-a708033cad35/image.png)

위 사진을 보면 노란색의 로직은 Class A, Class B, Class C에서 모두 중복된 로직들이다. 
하지만 요구사항이 들어와 노란색 로직을 바꾼다고 가정해보자, 그럼 우린 Class A, Class B, Class C 모든 클래스마다 공통적이게 수정을 해야할것이다.
이렇게 **어떤 로직을 기준으로 별도의 객체를 만들어 분리하는 기술을 AOP**라 한다.

### Spring AOP의 특징
- Bean에만 AOP 기술 적용 가능하다.
- Proxy 방식으로 AOP가 동작한다.

## 🤔 @Transactional의 동작 과정은?

@Transactional는 Spring AOP를 기반으로 동작한다. 
그래서 위에 특징으로 설명한것과 같이 Proxy 방식을 통해 동작한다.

![](https://velog.velcdn.com/images/sunggil-5125/post/81ad7213-799a-4392-8d0a-4834b34308c6/image.png)

위의 사진 처럼 대상 객체(Transaction을 적용할 로직)를 감싸는 Proxy 객체를 만들어 대상 객체의 결과에 따라 commit, rollback 한다. 위 사진을 코드로 바꾼다면 아래 코드 처럼 바뀔것이다.

```java
public class TransactionProxy{
    private final TransactonManager manager = TransactionManager.getInstance();
		...

    public void transactionLogic() {
        try {
            // 트랜잭션 전처리(트랜잭션 시작, autoCommit(false) 등)
			manager.begin();

			// 다음 처리 로직(타겟 비스니스 로직, 다른 부가 기능 처리 등)
			target.logic();
            
			// 트랜잭션 후처리(트랜잭션 커밋 등)
            manager.commit();
        } catch ( Exception e ) {
			// 트랜잭션 오류 발생 시 롤백
            manager.rollback();
        }
    }

```

### 💻 Proxy 객체를 만드는 방법은?

Proxy 객체를 만드는 방식으로는 2가지가 있다.

![](https://velog.velcdn.com/images/sunggil-5125/post/87b2e027-c8ae-45f5-abcf-be28d497ae0f/image.png)

- JDK Proxy 방식
Spring에서 사용하는 방식으로 Target 클래스의 인터페이스를 상속하여 Proxy 객체를 만든다. 
하지만 Target 클래스의 인터페이스가 존재하지 않는다면 JDK 방식에서는 Exception을 던져준다.

- CGLip Proxy
JDK 방식과는 달리 인터페이스가 없어도 Target 클래스를 상속하여 Proxy 객체를 만든다.
Target 클래스의 바이트 코드를 조작하여 Proxy 객체를 만들기 때문에 리플렉션 방식의 JDK Proxy보다 성능이 좋아 Spring Boot에서 사용한다.

## 🚨 @Transactional의 주의점

1. Target 메서드에 private 사용 불가 <br>
프록시 객체는 Target 객체, 인터페이스를 상속 받아 객체를 만들기 때문에 private로 되어있으면 상속 받을 수 없기 때문에 트랜잭션 관리가 되지 않는다.

2. Target 메서드에 내부적인 메서드를 사용하면  <br>
트랜잭션이 아닌 메소드에서 트랜잭션이 선언된 내부의 메소드를 호출하면 프록시 객체가 아닌 대상 객체의 메소드를 호출하기 때문에 트랜잭션이 적용되지 않는다.

```java
@Service
@RequiredArgsConstructor
public class PostService {
	private final PostRepository postRepository;

	public void savePostList(List<PostDto> postListDto) {
      	postListDto.forEach(postDto -> addBook(postDto));
    }
  
    @Transactional
    public void savePost(PostDto postDto) {
        Post post = postDto.toEntity();
        postRepository.save(post);
    }

}

```

~~구린 코드이지만 설명을 위해서..~~
위에 코드 처럼 @Transaction 어노테이션을 내부 메서드에 선언하면 프록시 객체가 savePost를 타겟 메서드로 삼기