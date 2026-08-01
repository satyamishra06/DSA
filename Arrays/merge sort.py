class Solution:
    def mergeSort(self, arr, l, r):
        # code here
        if l >= r:
            return
        mid = (l+r)//2
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        self.merge(arr,l,mid,r)
    def merge(self,arr,l,mid,r):
        result =[]
        i=l
        j=mid+1
        while i<=mid and j<=r:
            if arr[i]<arr[j]:
                result.append(arr[i])
                i+=1
            else:
                result.append(arr[j])
                j+=1
        while i<=mid:
            result.append(arr[i])
            i+=1
        while j <=r:
            result.append(arr[j])
            j+=1
        k=l
        for num in result:
            arr[k]=num
            k+=1
        