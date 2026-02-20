#include <iostream>
using namespace std;
int partition(int a[],int lb,int ub){
    int pivot = a[lb];
    int start = lb;
    int end = ub;
    while(start<end){
        while(a[start]<=pivot){
            start++;
        }
        while(a[end]>pivot){
            end--;
        }
        if(start<end){
            swap(a[start],a[end]);
        }
    }
    swap(a[lb],a[end]);
    return end;
}
void quicksort(int a[],int lb,int ub){
    if(lb<ub){
        int loc = partition(a,lb,ub);
        quicksort(a,lb,loc-1);
        quicksort(a,loc+1,ub);
    }   
}
int main() {
int k;
cout<<"Enter size of array(Quick Sort): ";
cin>>k;
int arr[k]={};
cout<<"Enter "<<k<<" elements: "; 
for(int i=0;i<k;i++){
    cin>>arr[i];
}
quicksort(arr,0,k-1);
for(int i=0;i<k;i++){
    cout<<arr[i]<<"-";
}
cout<<"NULL";
return 0;
}