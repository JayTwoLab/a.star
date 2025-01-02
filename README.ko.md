### `A*(A star)` 알고리즘: 효율적인 최단 경로 탐색 알고리즘

- `A*(A star)` 알고리즘은 그래프 탐색 및 경로 탐색 알고리즘으로, 효율적이고 최단 경로를 찾아주는 특성이 있습니다. 
- 주로 네비게이션 시스템, 게임 AI, 로봇 경로 계획 등에 사용됩니다. 
- A* 알고리즘은 다익스트라 알고리즘과 유사하지만, **휴리스틱(heuristic)** 을 사용하여 탐색을 더 효율적으로 만듭니다.

---

### `A*` 알고리즘의 주요 구성 요소

1. **노드 비용 (`g(n)`)**
   - 시작 노드에서 현재 노드까지의 실제 이동 비용.

2. **휴리스틱 (`h(n)`)**
   - 현재 노드에서 목표 노드까지의 예상 비용. (문제에 따라 유클리드 거리, 맨해튼 거리 등을 사용)

3. **평가 함수 (`f(n)`)**
   - \( `f(n) = g(n) + h(n)` \)
   - 총 비용으로, 이 값을 기준으로 탐색 우선순위를 정합니다.

---

### 작동 원리

1. **초기화**
   - 시작 노드를 `열린 목록(open list)`에 추가.
   - `닫힌 목록(closed list)`는 비워 둠.

2. **반복 과정**
   - 열린 목록에서 \( `f(n)` \) 값이 가장 낮은 노드를 선택.
   - 해당 노드가 목표 노드라면 탐색 종료.
   - 선택된 노드를 닫힌 목록에 추가.
   - 선택된 노드의 인접 노드들에 대해 다음을 수행:
     - 이미 닫힌 목록에 있으면 무시.
     - 열린 목록에 없으면 추가하고 \( `g(n)`, `h(n)`, `f(n)` \) 값을 계산.
     - 열린 목록에 있으면 \( `g(n)` \) 값이 더 작은 경우 업데이트.

3. **종료**
   - 목표 노드에 도달하면 경로를 반환.
   - 열린 목록이 비었지만 목표 노드에 도달하지 못하면 경로 없음.

---

### 의사 코드
> python
```
def main():
    # 그래프 정의 (노드: {이웃 노드: 거리})
    graph = {
        (0, 0): {(0, 1): 1, (1, 0): 1},
        (0, 1): {(0, 0): 1, (1, 1): 1},
        (1, 0): {(0, 0): 1, (1, 1): 1},
        (1, 1): {(0, 1): 1, (1, 0): 1, (2, 2): 2},
        (2, 2): {(1, 1): 2}
    }

    start = (0, 0)
    goal = (2, 2)

    path = a_star(graph, start, goal, heuristic)
    if path:
        print("최단 경로:", path)
    else:
        print("경로를 찾을 수 없습니다.")

if __name__ == "__main__":
    main()
```

- 상세 코드 : https://github.com/j2doll/a.star

- 코드 설명

<p align="center"> <img width="70%"  src="https://gist.githubusercontent.com/j2doll/36975662784b338d0b36ab12ea29fc5e/raw/dd99d47e5d9067eec4cb7129b5512d43461180cc/output%2520(1).png" /> </p>

A* 알고리즘은 최적의 경로를 탐색하는 알고리즘이지만, **최적의 경로가 여러 개 존재**할 경우에도 동일한 휴리스틱과 비용 조건에서 **하나의 경로만 반환**합니다. 

주어진 그래프에서 `(0, 0)`에서 시작해 `(1, 0)`을 경유하여 `(1, 1)`과 `(2, 2)`로 가는 경로가 최단 경로로 가능한지 확인하려면 각 경로의 총 비용을 계산해 봐야 합니다.

#### 1. 현재 경로 (A* 알고리즘이 반환한 경로)
- `(0, 0) → (0, 1) → (1, 1) → (2, 2)`
- 비용 계산:
  - `(0, 0) → (0, 1)`: 비용 1
  - `(0, 1) → (1, 1)`: 비용 1
  - `(1, 1) → (2, 2)`: 비용 2
  - **총 비용 = 1 + 1 + 2 = 4**

#### 2. 다른 경로 (경유지 추가)
- `(0, 0) → (1, 0) → (1, 1) → (2, 2)`
- 비용 계산:
  - `(0, 0) → (1, 0)`: 비용 1
  - `(1, 0) → (1, 1)`: 비용 1
  - `(1, 1) → (2, 2)`: 비용 2
  - **총 비용 = 1 + 1 + 2 = 4**

#### 분석 결과
두 경로의 총 비용은 동일합니다. 따라서 `(0, 0)`에서 `(1, 0)`을 경유하여 `(1, 1)`과 `(2, 2)`로 가는 경로도 최단 경로로 가능합니다.

#### `A*` 알고리즘의 특성
- `A*` 알고리즘은 **하나의 최단 경로만 반환** 하기 때문에, 동일한 비용의 다른 최단 경로는 탐색 과정에서 선택되지 않을 수 있습니다.
- 여러 최단 경로를 모두 찾으려면 알고리즘을 약간 수정하거나, BFS와 같은 다른 접근법을 사용해야 합니다.


---

### `A*` 알고리즘의 장점
1. **최적성**: \( `h(n)` \)이 **허용적**(`admissible`) 이고, **일관성**(`consistent`) 을 만족하면 항상 최단 경로를 보장.
2. **효율성**: 불필요한 경로 탐색을 줄이기 때문에 빠름.

### 사용 예시
1. **게임 개발**: 유닛이 장애물을 피해 목표 지점으로 이동할 때.
2. **로봇 공학**: 로봇 경로 계획.
3. **네비게이션 시스템**: 차량 경로 탐색.