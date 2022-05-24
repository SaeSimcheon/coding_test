## 다익스트라

- single source
- 그리디 알고리즘

- 최초 시간 복잡도 

$$O(V^2)$$

- 우선순위 큐(=힙 트리)등을 이용한 개선 이후 시간 복잡도 

$$O((V+E)logV)$$

  ```
  - (V는 정점의 개수, E는 한 정점의 주변 노드)
  - 각 노드마다 미방문 노드 중 출발점으로부터 현재까지 계산된 최단 거리를 가지는 노드를 찾는데 O(VlogV)의 시간. 
  - 각 노드마다 이웃한 노드의 최단 거리를 갱신할 때 O(ElogV).
  ```
## 구현 팁
- python에서는 heapq를 이용하여 쉽게 구할 수 있음.
- defaultdict를 이용하여 key가 없는 경우에 대해 따로 조건문을 사용하지 않고 구현하는 것이 편리한 경우가 있음.
  ```python
  # 이런 방식으로 default value를 custom할 수도 있음.
  def ftn():
    return 'a'
  defaultdict(ftn)
  ```
  



## [플로이드 와샬](https://ko.wikipedia.org/wiki/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)

- 모든 노드에서 각 노드에 방문할 수 있는 최단 경로를 구하는 알고리즘. 동적 계획법의 한 예.


시간 복잡도 
$$O(|V|^3)$$


- for 문 3개로 이루어지며. 경유지가 가장 위에 와야함.
- 두 꼭짓점 간의 추정 최단 경로를 최적이 될 때까지 개선.
- [음수 사이클에도 적용가능.](https://ko.wikipedia.org/wiki/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)




### 알고리즘
- 1부터 N까지 각 node에 번호가 매겨진 그래프를 가정.
- i에서 j로 집합 {1,...,k}의 node들 만들 경유지로 거쳐 최단 경로를 반환하는 함수를 $shortestpath(i,j,k)$로 가정.
- $shortestpath(i,j,k)$는 다음 중 한 가지에 속함.
```
(1) k를 통과하지 않는 경로
(2) k를 통과하는 경로
```
i에서 k를 거쳐 j로 가는 더 나은 경로가 있다면,  그 경로는 i-> k 와 k-> j(모두 1에서 k-1까지만을 거침) 가는 경로를 합친 것.

$$
shortestpath(i,j,0) = weight(i,j)
$$

$$
shortestpath(i,j,k) = min(shortestpath(i,j,k-1),shortestpath(i,k,k-1)+shortestpath(k,j,k-1))
$$

## 벨만-포드 알고리즘
- [나무위키](https://namu.wiki/w/%EB%B2%A8%EB%A8%BC-%ED%8F%AC%EB%93%9C%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)
- [](https://iamcoder.wiki/w/Bellman-Ford%20Algorithm/)
- [](https://ratsgo.github.io/data%20structure&algorithm/2017/11/27/bellmanford/)
