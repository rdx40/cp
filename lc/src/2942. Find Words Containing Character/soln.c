int* findWordsContaining(char** words, int wordsSize, char x, int* returnSize) {
    int* ret = (int*)malloc(wordsSize*sizeof(int));
    int cnt=0;

    for(int i=0;i<wordsSize;i++){
        if(strchr(words[i],x)){
            ret[cnt++] = i;
        }
    }
    *returnSize = cnt;
    return ret;
}
