#include<bits/stdc++.h>
#define ll long long int
using namespace std ;

void bfs(int src,int dst,vector<vector<ll>>adj) {

    queue<vector<ll>>q ;
    vector<ll>v;
    
    v.push_back(0) ;
    
    q.push(v) ;

    while (!q.empty())
    {
        v = q.front() ;
        q.pop() ;
        int last = v[v.size()-1] ;

        if(last == dst) {
            for (ll i = 0; i < v.size(); i++)
            {
                    cout<<char(v[i]+'A')<<" " ;
            }
            cout<<endl;
        }

        for (ll i = 0; i < adj[last].size(); i++)
        {
                if(find(v.begin(),v.end(),adj[last][i]) == v.end()) {
                    vector<ll>newPath(v) ;
                    newPath.push_back(adj[last][i]) ;
                    q.push(newPath) ;
                }
        }
        
    }
    
    
     
}


void dfs(int i,int dst,vector<ll>v,vector<ll>vis,vector<vector<ll>>adj) {

    vis[i] = 1 ;

    if(i == dst){
            for (ll ii = 0; ii < v.size(); ii++)
            {
                    cout<<char(v[ii]+'A')<<" " ;
            }
            cout<<endl;
            return ;
    }

    for (ll j = 0; j < adj[i].size(); j++)
    {
        if(!vis[adj[i][j]]) {
          
            v.push_back(adj[i][j]) ;
            dfs(adj[i][j],dst,v,vis,adj) ;
            v.pop_back() ;
           
        }
    }
    
    vis[i] = 0 ;
     
}

int main(){
   ios::sync_with_stdio(0);
   cin.tie(0);  


    ll n = 9 , dst = 'E'-'A', src = 0 ;
    vector<vector<ll>>adj(26);

    adj['A'-'A'].push_back('B'-'A') ;
    adj['B'-'A'].push_back('A'-'A') ;

    adj['A'-'A'].push_back('S'-'A') ;
    adj['S'-'A'].push_back('A'-'A') ;

    adj['C'-'A'].push_back('S'-'A') ;
    adj['S'-'A'].push_back('C'-'A') ;

    adj['C'-'A'].push_back('D'-'A') ;
    adj['D'-'A'].push_back('C'-'A') ;

    adj['C'-'A'].push_back('F'-'A') ;
    adj['F'-'A'].push_back('C'-'A') ;

    adj['C'-'A'].push_back('E'-'A') ;
    adj['E'-'A'].push_back('C'-'A') ;

    adj['S'-'A'].push_back('G'-'A') ;
    adj['G'-'A'].push_back('S'-'A') ;

    adj['H'-'A'].push_back('G'-'A') ;
    adj['G'-'A'].push_back('H'-'A') ;

    adj['H'-'A'].push_back('E'-'A') ;
    adj['E'-'A'].push_back('H'-'A') ;

    adj['F'-'A'].push_back('G'-'A') ;
    adj['G'-'A'].push_back('F'-'A') ;
  
    vector<ll>vis(26,0) ;
    vector<ll>v ;

    cout<<"BFS : "<<endl;
    bfs(src,dst,adj) ;


    cout<<"\nDFS : "<<endl;
    v.push_back(0) ;
    dfs(0,dst,v,vis,adj) ;
   
}
