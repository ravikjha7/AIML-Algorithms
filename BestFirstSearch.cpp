/******************************************************************************

Q2. Find Best first Search or the following graph from A to I and find total cost function as well

*******************************************************************************/
#include <bits/stdc++.h>

using namespace std;

int main()
{
    vector<vector<pair<int,int>>> gp(11);
    gp[0].push_back(make_pair(3,1));
    gp[0].push_back(make_pair(4,9));
    gp[0].push_back(make_pair(1,6));
    gp[1].push_back(make_pair(10,3));
    gp[9].push_back(make_pair(3,3));
    gp[6].push_back(make_pair(8,5));
    gp[6].push_back(make_pair(14,4));
    gp[5].push_back(make_pair(2,8));
    gp[5].push_back(make_pair(2,4));
    gp[4].push_back(make_pair(1,8));
    gp[3].push_back(make_pair(11,7));
    gp[7].push_back(make_pair(4,5));
    gp[7].push_back(make_pair(3,2));
    
    // cout<<gp[5][1].second;
    
    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>>pr;
    pr.push(gp[0][0]);
    pr.push(gp[0][1]);
    pr.push(gp[0][2]);
    int final = 8;
    vector<char>aa = {'A','B','C','D','E','F','G','H','I','J'};
    cout<<aa[0]<<"->";
    while(!pr.empty()){
        int cost = pr.top().first;
        int node = pr.top().second;
        pr.pop();
        cout<<aa[node];
        if(node == final){
            cout<<endl;
            cout<<"Total Cost is:"<<cost<<endl;
            break;
        }
        cot<<"->";
        for(auto it:gp[node]){
            int cst = it.first + cost;
            int nd = it.second;
            pr.push(make_pair(cst,nd));
        }
    }
    return 0;
}