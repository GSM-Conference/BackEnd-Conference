# JpaRepository와 CrudRepository의 차이점
JpaRepository와 CrudRepository는 스프링 데이터 JPA에서 제공하는 인터페이스입니다.<br>
이 두 인터페이스는 데이터베이스와 상호 작용하기 위한 일반적인 메서드를 제공합니다.<br>
그러나 JpaRepository는 CrudRepository를 상속받아 더 많은 기능을 추가로 제공합니다.

## CrudRepository
CrudRepository는 CRUD 작업을 수행하기 위한 기본적인 메서드를 가지고 있습니다.
이 인터페이스는 데이터베이스의 레코드를 생성, 조회, 수정, 삭제하는 데 사용됩니다.

```kotlin
public interface AccountRepository extends CrudRepository<Account, Long> {

}

// 인터페이스가 비어 있어도, 아래의 메서드들은 호출이 가능
<S extends T> S save(S entity);

Optional<T> findById(ID id);

Iterable<T> findAll();

long count();

void deleteById(ID id);
```

## JpaRepository
JpaRepository는 `CrudRepository`와 `PaginAndSortingRepository`를 `extends`한 인터페이스입니다.<br>

`CrudRepository`(Crud)와 `PagingAndSortingRepository`(페이징 및 정렬)가 제공하는 모든 기능을 제공하고, 추가적으로 JPA에 특성화된 메서드를 제공한다.

JpaRepository는 보다 더 좋은 기능을 제공합니다.<br>
예를 들어, `findAll()` 메서드는 데이터베이스의 모든 레코드를 조회합니다. `findBy...()` 메서드는 특정 조건을 만족하는 레코드를 조회할 수 있습니다. 이런 추가 메서드를 통해 개발자는 더욱 간편하게 데이터베이스 작업을 수행할 수 있습니다.

JpaRepository는 이렇게 더 좋은 기능을 제공함으로, 대부분의 프로젝트에서는 JpaRepository를 사용합니다. 그러나 CrudRepository만으로 충분히 구현 가능한 경우에는 더 가벼운 인터페이스로서 CrudRepository를 선택할 수도 있습니다.

## 무조건 JpaRepository?
고급 쿼리 기능이 필요하지 않은 소규모 또는 덜 복잡한 프로젝트의 경우 CrudRepository가 적합할 수 있습니다. 데이터 액세스에 대한 단순하고 최소한의 접근 방식을 제공하여 코드베이스를 간결하고 집중적으로 유지합니다.

## 사용
+ CrudRepository: NoSQL 데이터베이스 또는 메모리 내 컬렉션과 같은 비 JPA 데이터 소스에 대한 간단한 CRUD 작업입니다.
+ JpaRepository: 쿼리 메서드, 페이지 매김 및 정렬과 같은 JPA 관련 기능을 활용하여 JPA 구현으로 작업합니다.

## 차이점
+ CrudRepository: save(), findById(), findAll(), delete() 등과 같은 표준 CRUD 작업을 제공합니다. 데이터 소스와 상호 작용하는 일반적인 접근 방식을 제공하며 JPA에 국한되지 않습니다.
+ JpaRepository: CrudRepository에서 상속받은 CRUD 작업 외에 JPA 고유의 기능을 제공합니다. 여기에는 쿼리 메서드(메소드 이름을 기반으로 쿼리 자동 생성), 쿼리 결과의 페이지 매김 및 정렬, 지속성 컨텍스트 플러시 및 지우기, 관련 엔터티의 열망 및 지연 로드 제어, 수명 주기 이벤트에 대한 엔터티 리스너 등록이 포함됩니다.
