//
//  main.cpp
//  PS_cpp
//
//  Created by 권보성 on 9/24/25.
//

#include <iostream>
using namespace std;
int main(){
    int L, A, B, C, D;
    cin >> L;
    cin >> A;
    cin >> B;
    cin >> C;
    cin >> D;
    int korean = 0;
    int math = 0;
    korean += A/C;
    if (A%C != 0){
        korean += 1;
    }
    math += B/D;
    if(B%D!=0){
        math += 1;
    }
    if (korean >= math){
        cout << L - korean << endl;
    }
    else{
        cout << L - math << endl;
    }
}
