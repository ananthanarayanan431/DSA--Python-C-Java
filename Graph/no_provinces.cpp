
#include<bits/stdc++.h>

using namespace std;


void dfs(int src,vector<vector<int>> arr,vector<int>& vis,int n,int m) {
    vis[src]=true;

    for (int j=0; j<m; ++j) {
        if (arr[src][j] && !vis[j]) {
            dfs(j,arr,vis,n,m);
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<vector<int>> isConnected = {
        {1, 0, 0},
        {0, 1, 0},
        {0, 0, 1}
    };

    int n=isConnected.size();
    int m=isConnected[0].size();

    vector<int> vis(n,false);
    int count=0;

    for (int i=0; i<n; ++i) {
        if (!vis[i]) {
            count++;
            dfs(i,isConnected,vis,n,m);
        }
    }
    cout<<count<<endl;
    return 0;
}