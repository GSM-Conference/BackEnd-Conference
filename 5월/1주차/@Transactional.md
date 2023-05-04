# **선언적 트랜잭션 @Transactionnal**

<br>

## **트랜잭션이란?**
데이터베이스의 상태를 변경시키는 작업 또는 한번에 수행되어야하는 연산들을 의미한다.  
트랜잭션 작업이 끝나면 Commit 또는 Rollback 되어야한다.

<br>

## **트랜잭션의 성질**

|원자성(Atomicity)|
|--|
|한 트랜잭션 내에서 실행한 작업들은 하나의 단위로 처리합니다 즉,모두 성공 또는 모두 실패|

|일관성(Consistency)|
|--|
|트랜잭션은 일관성 있는 데이터베이스 상태를 유지한다.|

|격리성(Isolation)|
|--|
|동시에 실행되는 트랜잭션들이 서로 영향을 미치지 않도록 격리해야한다.|

|영속성(Durability)|
|--|
|트랜잭션을 성공적으로 처리되면 결과가 항상 저장되어야한다.|

<br>

## **@Transactional**
스프링에서 지원하는 **선언적 트랜잭션**이다. xml 또는 Javaconfig를 통해 설정 할 수 있다.   
Spring boot에서는 별도의 설정이 필요 없으며, 클래스 또는 메소드에 선언할 수 있다.

```java
import com.example.bamdule.service.UserService;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@Transactional
//@Transactional(propagation = , isolation = ,noRollbackFor = ,readOnly = ,rollbackFor = ,timeout = )
public class UserServiceImpl implements UserService {
...
}
```

<br>

## **@Transactional 옵션**

|propagation|
|--|
|트랜잭션 동작 도중 다른 트랜잭션을 호출할 때, 어떻게 할 것인지 지정하는 옵션이다|

|isolation|
|--|
|트랜잭션에서 일관성없는 데이터 허용 수준을 설정한다|

|noRollbackFor=Exception.class|
|--|
|특정 예외 발생 시 rollback하지 않는다.|

|rollbackFor=Exception.class|
|--|
|특정 예외 발생 시 rollback한다.|

|timeout|
|--|
|지정한 시간 내에 메소드 수행이 완료되지 않으면 rollback 한다. (-1일 경우 timeout을 사용하지 않는다)|

|readOnly|
|--|
|트랜잭션을 읽기 전용으로 설정한다.|

<br>

### **1. propagation**
|REQUIRED (Default)|
|--|
|이미 진행중인 트랜잭션이 있다면 해당 트랜잭션 속성을 따르고, 진행중이 아니라면 새로운 트랜잭션을 생성한다.|

|REQUIRES_NEW|
|--|
|항상 새로운 트랜잭션을 생성한다. 이미 진행중인 트랜잭션이 있다면 잠깐 보류하고 해당 트랜잭션 작업을 먼저 진행한다.|

|SUPPORT|
|--|
|이미 진행중인 트랜잭션이 있다면 해당 트랜잭션 속성을 따르고, 없다면 트랜잭션을 설정하지 않는다.|

|NOT_SUPPORT|
|--|
|이미 진행중인 트랜잭션이 있다면 보류하고, 트랜잭션 없이 작업을 수행한다.|

|MANDATORY|
|--|
|이미 진행중인 트랜잭션이 있어야만, 작업을 수행한다. 없다면 Exception을 발생시킨다.|

|NEVER|
|--|
|트랜잭션이 진행중이지 않을 때 작업을 수행한다. 트랜잭션이 있다면 Exception을 발생시킨다.|

|NESTED|
|--|
|진행중인 트랜잭션이 있다면 중첩된 트랜잭션이 실행되며, 존재하지 않으면 REQUIRED와 동일하게 실행된다.|

<br>

### **2. isolation**
|Default|
|--|
|사용하는 DB 드라이버의 디폴트 설정을 따른다. 대부분 READ_COMMITED를 기본 격리수준으로 설정한다.

|READ_COMMITED|
|--|
|트랜잭션이 커밋하지 않은 정보는 읽을 수 없다. 하지만 트랜잭션이 읽은 로우를 다른 트랜잭션에서 수정 할 수 있다 그래서 트랜잭션이 같은 로우를 읽었어도 시간에 따라서 다른 내용이 발견될 수 있다.|

|READ_UNCOMMITED|
|--|
|가장 낮은 격리 수준이다. 트랜잭션이 커밋되기 전에 그 변화가 다른 트랜잭션에 그대로 노출된다. 하지만 속도가 빠르기 때문에 데이터의 일관성이 떨어지더라도, 성능 극대화를 위해 의도적으로 사용하기도 한다.|

|REPEATABLE_READ|
|--|
|트랜잭션이 읽은 로우를 다른 트랜잭션에서 수정되는 것을 막아준다. 하지만 새로운 로우를 추가하는 것은 제한하지 않는다.|

|SERIALIZABLE|
|--|
|가장 강력한 트랜잭션 격리수준이다. 여러 트랜잭션이 동시에 같은 테이블 로우에 엑세스하지 못하게 한다. 가장 안전하지만 가장 성능이 떨어진다.|

<br>

### **3. rollbackFor**
트랜잭션 작업 중 런타임 예외가 발생하면 롤백한다. 반면에 예외가 발생하지 않거나 체크 예외가 발생하면 커밋한다.   

체크 예외를 커밋 대상으로 삼는 이유는 체크 예외가 예외적인 상황에서 사용되기 보다는 리턴 값을 대신해서 비지니스 적인 의미를 담은 결과로 돌려주는 용도로 사용되기 때문이다.

스프링에서는 데이터 엑세스 기술의 예외를 런타임 예외로 전환해서 던지므로 런타임 예외만 롤백대상으로 삼는다.

하지만 원한다면 체크예외지만 롤백 대상으로 삼을 수 있다. rollbackFor또는 rollbackForClassName 속성을 이용해서 예외를 지정한다.

<br>

### **4. noRollbackFor**
rollbackFor 속성과는 반대로 런타임 예외가 발생해도 지정한 런타임 예외면 커밋을 진행한다.

<br>

### **5. timeout**
트랜잭션에 제한시간을 지정한다. 초 단위로 지정하고, 디폴트 설정으로 트랜잭션 시스템의 제한 시간을 따른다.

-1 입력시, 트랜잭션 제한시간을 사용하지 않는다.

<br>

### **6. readOnly**
트랜잭션을 읽기 전용으로 설정한다. 특정 트랜잭션 안에서 쓰기 작업이 일어나는 것을 의도적으로 방지하기 위해 사용된다. insert, update, delete 작업이 진행되면 예외가 발생한다.





