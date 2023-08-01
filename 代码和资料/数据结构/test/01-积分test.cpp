#include<iostream>
using namespace std;


double func(double x){
    return x * x;
}


double getsum(double s,double e,int n,double (*fun)(double)){
    double ans = 0;
    double step = (e - s) / n;

    while(s<e){
        ans += fun(s) * step;
        s += step;
    }

    return ans;
}

double jifen(double s,double e){
    double n = 1000;
    double s1 = 0,s2 = 0;
    const double E = 1e-4;

    s1 = getsum(s, e, n, func);

    while(1){

        n *= 2;
        s2 = getsum(s, e, n, func);

        cout << s1 << " " << s2 <<endl;

        if(abs(s1-s2)<E){
            break;
        }

        s1 = s2;

        
    }

    return s2;
}

int main(){

    cout << jifen(0, 100) << endl;
}