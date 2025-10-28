#include <iostream>
#include <string.h>
using namespace std;
int main(){
    int num;
    cin >> num;
    string str;
    cin >> str;
    int flag = 0;
    for(int i = 0; i< num-4;i++){
        char last = str[i];
        int count = 1;
        for (int j = 1; j<5;j++){
            if(last-str[i+j] == 1 || last-str[i+j] == -1){
                last = str[i+j];
                count ++;
            }
            else{
                break;
            }
        }
        if(count == 5){
            flag = 1;
        }
    }
    if (flag == 1){
        cout << "YES" << endl;
    }
    else {
        cout << "NO" << endl;
    }

}
