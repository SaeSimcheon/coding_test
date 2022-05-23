## 다익스트라




## [플로이드 와샬](https://ko.wikipedia.org/wiki/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)

- 모든 노드에서 각 노드에 방문할 수 있는 최단 경로를 구하는 알고리즘. 동적 계획법의 한 예.
- 시간 복잡도 $O(|V|^3)$
- for 문 3개로 이루어지며. 경유지가 가장 위에 와야함.
- 두 꼭짓점 간의 추정 최단 경로를 최적이 될 때까지 개선.
- [음수 사이클에도 적용가능.](https://ko.wikipedia.org/wiki/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)

$$
shortestpath(i,j,0) = weight(i,j)
$$

$$
shortestpath(i,j,k) = min(shortestpath(i,j,k-1),shortestpath(i,k,k-1)+shortestpath(k,j,k-1))
$$
