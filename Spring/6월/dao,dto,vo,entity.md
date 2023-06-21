# DAO, DTO, VO, Entity 란?

## DAO (Data Access Object)

* 실제 DB에 접근하여 CRUD 등의 작업을 수행하는 객체

```java
public interface PostRepository extends JpaRepository<Post, Long> {
    void deleteByUser(User user);
}
```

> JPA의 경우 JpaRepository 가 DAO 의 예시라고 생각하면 된다.

## DTO (Data Transfer Object)

* 계층간의 데이터 교환을 위해 Data를 변환해서 사용하는 객체
    * 로직을 갖지 않으며, Getter/Setter로 이루어져 있다.

```java
@Getter
@Setter
public class WritePostRequest {

    private String title;
    
    private String content;
    
    private List<String> category;

}
```

## VO (Value Object)

* Read-Only 속성의 DTO

```java
@Getter
public class WritePostRequest {

    private String title;
    
    private String content;
    
    private List<String> category;

}
```

> Read-Only 이기 때문에 Setter가 없다.

## Entity

* 실제 DB Table과 매핑되는 클래스
* `@Entity` 어노테이션을 붙여 사용하며 Setter를 지양한다.
    * Setter를 지양하는 이유
        * Create 목적인지 Update 목적인지 불분명하다.
        * 일관성을 보장하기 어렵다. -> Builder 패턴 권장


```java
@Entity
@Getter @Builder
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@AllArgsConstructor
public class Post {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "post_id")
    private Long postId;

    @Column(name = "title", nullable = false, length = 30)
    private String title;

    @Column(name = "content", nullable = false, length = 500)
    private String content;

    @ElementCollection(fetch = FetchType.EAGER)
    private List<Category> category;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "member_id")
    private Member member;

}
```

> JPA 에서 기본 생성자를 필요로 하는데, protected로 제어하는 것을 허용해줘서 `@NoArgsConstructor(access = AccessLevel.PROTECTED)
` 로 객체 일관성을 유지시키는 것이 좋다.