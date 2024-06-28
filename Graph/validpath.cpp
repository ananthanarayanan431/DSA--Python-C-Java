
#include<bits/stdc++.h>

using namespace std;

bool dfs(vector<vector<bool>>& graph,int src,int des,vector<bool>& vis,int n) {
    if (src==des){
        return true;
    }
    for (int i=0; i<n; ++i) {
        if (graph[src][i] && !vis[i]) {
            return true;
        }
    }
    return false;
}

bool validpath(int n,vector<vector<int>>& edges, int src,int des) {

    vector<vector<bool>> graph(n, vector<bool> (n,false));

    for (auto edge: edges) {
        int u=edge[0];
        int v=edge[1];

        graph[u][v]=true;
        graph[v][u]=true;
    }
    vector<bool> vis (n,false);
    return dfs(graph,src,des,vis,n);
}

int main() 
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n=3;
    vector<vector<int>> edges = {{0,1},{1,2},{2,0}};
    int src=0;
    int dec=2;

    cout<<validpath(n,edges,src,dec);
    return 0;
}