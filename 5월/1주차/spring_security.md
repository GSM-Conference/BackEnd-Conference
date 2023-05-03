# Spring Security

> 스프링 기반의 애플리케이션의 보안을 담당하는 스프링 하위 프레임워크

## 보안 언어

* 인증 (Authenticate) : 접근하려는 유저가 누구인지 확인하는 것
  * Ex: 로그인
* 인가 (Authorization) : 인증된 사용자에 대해 권한을 확인하고 허락하는 것
* 접근 주체 (Principal) : 보호된 대상에 접근하는 유저
* 비밀번호 (Credential) : 대상에 접근하는 유저의 비밀번호

> 인증과 인가의 차이를 쉽게 설명하자면, 인증은 로그인이고 인가는 로그인을 한 후에 일로 이해하면 된다.

> Spring security에서 인증, 인가를 위해 Principal 은 아이디, Credential은 비밀번호로 사용하는 `Credential 기반의 인증 방식`을 사용한다.

## Spring Security 모듈

### SecurityContextHolder
<img src = "https://github.com/JuuuuHong/TIL/raw/bf53991a4b67c73f610f44e688236633f06df0a7/image/securitycontextholder.png">

* SecurityContext를 제공하는 static 메서드를 지원한다.

### SecurityContext

* Authentication을 보관하는 역할이다.

### Authentication

```java
public interface Authentication extends Principal, Serializable {
    // 현재 사용자의 권한 목록을 가져옴
    Collection<? extends GrantedAuthority> getAuthorities();
    
    // credentials(주로 비밀번호)을 가져옴
    Object getCredentials();
    
    // 사용자 상세정보
    Object getDetails();
    
    // Principal(주로 ID) 객체를 가져옴.
    Object getPrincipal();
    
    // 인증 여부를 가져옴
    boolean isAuthenticated();
    
    // 인증 여부를 설정함
    void setAuthenticated(boolean isAuthenticated) throws IllegalArgumentException;
}
```

### UsernamePasswordAuthenticationToken

> Authentication을 implements한 AbstractAuthenticationToken의 하위 클래스로, ID는 Principal, Password는 Credential의 역할을 한다.

```java
public class UsernamePasswordAuthenticationToken extends AbstractAuthenticationToken {
    
    // 주로 사용자의 ID
    private final Object principal;
    
    // 주로 사용자의 password
    private Object credentials;
    
    // 인증 완료 전의 객체 생성
    public UsernamePasswordAuthenticationToken(Object principal, Object credentials) {
        super(null);
        this.principal = principal;
        this.credentials = credentials;
        setAuthenticated(false);
    }
    
    // 인증 완료 후의 객체 생성
    public UsernamePasswordAuthenticationToken(Object principal, Object credentials, Collection<? extends GrantedAuthority> authorities) {
        super(authorities);
        this.principal = principal;
        this.credentials = credentials;
        super.setAuthenticated(true);
    }
    
}

public abstract class AbstractAuthenticationToken implements Authentication, CredentialsContainer {
}
```

* UsernamePasswordAuthenticationToken(Object principal, Object credentials) : 인증 전의 객체를 생성
* UsernamePasswordAuthenticationToken(Object principal, Object credentials,Collection<? extends GrantedAuthority> authorities) : 인증 완료된 객체를 생성

### AuthenticationProvider

```java
public interface AuthenticationProvider {

	// 인증 전의 Authentication 객체를 받아서 인증된 Authentication 객체를 반환
    Authentication authenticate(Authentication var1) throws AuthenticationException;

    boolean supports(Class<?> var1);
    
}
```

* AuthenticationProvider 에서는 실제 인증에 대한 부분을 처리한다.
* Authentication는 인증이 완료된 객체를 반환한다.
* Authentication 인터페이스를 구현해서 Custom Authentication Provider를 작성해서, AuthenticationManager에 등록하면 된다.

### AuthenticationManager

```java
public interface AuthenticationManager {
	Authentication authenticate(Authentication authentication) 
		throws AuthenticationException;
}
```

* 인증에 대한 부분을 처리하는 인터페이스  
  * 실질적으로는 AuthenticationManager에 등록된 AuthenticationProvider에 의해 처리된다.
* 인증에 성공하면 2번째 생성자를 이용해 SecurityContext에 저장한다
  * 인증 상태를 유지하기 위해 세션에 저장한다.
* 인증이 실패하면 AuthenticationException을 발생시킨다.

### UserDetailsService

```java
public interface UserDetailsService {

    UserDetails loadUserByUsername(String username) throws UsernameNotFoundException;

}
```

* UserDetails 객체를 반환하는 하나의 메서드를 가지고 있다.
* 보통 이를 구현한 클래스에서는 UserRepository를 주입받아서 DB와 연결하여 처리한다.

### UserDetails

```java
public interface UserDetails extends Serializable {

    Collection<? extends GrantedAuthority> getAuthorities();

    String getPassword();

    String getUsername();

    boolean isAccountNonExpired();

    boolean isAccountNonLocked();

    boolean isCredentialsNonExpired();

    boolean isEnabled();
    
}
```

* 인증에 성공하여 생성된 UserDetails는 Authentication 객체를 구현한 UsernamePasswordAuthenticationToken을 생성하기 위해 사용된다.

### Password Encoding

```java
@Override
protected void configure(AuthenticationManagerBuilder auth) throws Exception {
	auth.userDetailsService(userDetailsService).passwordEncoder(passwordEncoder());
}

@Bean
public PasswordEncoder passwordEncoder() {
	return new BCryptPasswordEncoder();
}
```

> NoOpPasswordEncoder : deprecate 되었다.
>
> BCryptPasswordEncoder : bcrypt 해쉬 알고리즘을 이용 (스프링 버전5 부터는 의무적)
> 
> StandardPasswordEncoder : sha 해쉬 알고리즘을 이용

### GrantedAuthority

* GrantedAuthority는 현재 사용자(Principal)의 권한을 의미한다.
* GrantedAuthority 객체는 UserDetailsService에 의해 불러올 수 있고, 특정 자원에 대한 권한이 있는지를 검사하여 접근 허용 여부를 결정한다.

> ROLE_ADMIN / ROLE_USER 과 같은 형태로 사용하며 "roles" 라고 부른다.

## Spring Security Architecture

<img src = "https://github.com/JuuuuHong/TIL/raw/bf53991a4b67c73f610f44e688236633f06df0a7/image/securityarchitecture.png">

1. 사용자가 로그인 정보와 함께 인증 요청을 한다.
2. AuthenticationFilter가 요청을 가로채고, 가로챈 정보를 바탕으로 UsernamePasswordAuthenticationToken의 인증용 객체를 생성한다.
3. AuthenticationManager의 구현체인 ProviderManager에게 생성한 UsernamePasswordToken 객체를 전달한다.
4. AuthenticationManager는 등록된 AuthenticationProvider를 조회하여 인증을 요구한다.
5. 실제 DB에서 사용자 인증정보를 가져오는 UserDetailsService에 사용자 정보를 넘겨준다.
6. 넘겨받은 사용자 정보를 통해 DB에서 찾은 사용자 정보인 UserDetails 객체를 만든다.
7. AuthenticationProvider는 UserDetails를 넘겨받고 사용자 정보를 비교한다.
8. 인증이 완료되면 권한 등의 사용자 정보를 담은 Authentication 객체를 반환한다.
9. 다시 최초의 AuthenticationFilter에 Authentication 객체가 반환된다.
10. Authentication 객체를 SecurityContext에 저장한다.