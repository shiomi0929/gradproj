# -*- coding: utf-8 -*-
ForestDist[left(dI)−1][left(qJ)−1]=0
for i : left(dI) to I do
    ForestDist[i][left(qJ ) − 1] = ForestDist[i − 1][left(qJ ) −
1] + γ(di, ∧)
end for
for j : left(qJ) to J do
    ForestDist[left(dI ) − 1][j] = ForestDist[left(dI ) − 1][j − 1] + γ(∧, qj )
end for
for i : left(dI) to I do
    for j : left(qJ) to J do
        if left(di) = left(dI) and left(qj) = left(qJ) then
            di.TED[j] = ForestDist[i][j] = min(
                ForestDist[i − 1][j] + γ(di, ∧),
                ForestDist[i][j − 1] + γ(∧, qj ),
                ForestDist[i − 1][j − 1] + γ(di, qj )
            )
        else
            ForestDist[i][j] = min(
                ForestDist[i − 1][j] + γ(di, ∧),
                ForestDist[i][j − 1] + γ(∧, qj ),
                ForestDist[left(di)−1][left(qj)−1]+di.TED[j]
            )
        end if
    end for
end for