
#include<bits/stdc++.h>

using namespace std;

void housing(vector<int> plot,int n,int k) {
    int i=0;
    int j=0;
    int sumof=0;

    while (j<n) {
        sumof+=plot[j];
        j++;

        while (sumof>k and i<j){
            sumof-=plot[i];
            i++;
        }

        if(sumof==k){
            cout<<i<<" "<<j-1<<endl;
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<int> plots{1,3,2,1,4,1,3,2,1,1};
    int n=plots.size();
    int k=8;

    housing(plots,n,k);

    return 0;
}