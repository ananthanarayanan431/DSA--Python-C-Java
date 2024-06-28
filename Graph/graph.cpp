
#include<bits/stdc++.h>

using namespace std;

int main() 
{

    int n,m;
    cin>>n>>m;

    int adj1[n+1][n+1];
    // adjacency matrix for undirected graph

    for (int i=0; i<m; ++i) {
        int u,v;

        cin>>u>>v;
        adj1[u][v]=1;
        adj1[v][u]=1;
    }

    vector<int> adj[n+1];
    // adjacency list for undirected graph

    for (int i=0; i<n; ++i) {
        int u,v;
        cin>>u>>v;

        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<pair<int,int>> adj[n+1];
    return 0;
}