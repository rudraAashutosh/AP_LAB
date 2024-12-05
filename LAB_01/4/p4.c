#include <stdio.h>

void make_file()
{
    
   

FILE *inputFile = fopen("A:\\CODE\\Application_Programming\\LAB_01\\4\\add1.c", "r");
if (inputFile == NULL ) {
    printf("Error opening file input\n");
    return;
}

FILE *outputFile = fopen("A:\\CODE\\Application_Programming\\LAB_01\\4\\output.c", "w");
if (outputFile == NULL ) {
    printf("Error opening file output\n");
    return;
}
    int ch;
    while ((ch = fgetc(inputFile)) != EOF) {
        if (ch == '+') {
            fputc('*', outputFile);
        } else {
            fputc(ch, outputFile);
        }
    }

    fclose(inputFile);
    fclose(outputFile);
}

int main() {
    make_file();
    return 0;
}