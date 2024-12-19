import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); // N 입력 받기
        long mod = 1000000000; // 출력에서 mod 연산 할 수
        long D[] = new long[1000001]; // 최대 1,000,000개가 저장될 수 있도록 배열 크기 설정
        D[1] = 0; // 1개로 만들 수 있는 경우의 수는 0 (초기화)
        D[2] = 1; // 2개로 만들 수 있는 경우의 수는 1 (초기화)
        
        for(int i = 3; i<=N;i++){
            // 식을 이용하여 D[i] 값 계산
            D[i] = (i-1)*(D[i-1]+D[i-2])%mod;
        }
        //결과값 출력
        System.out.println(D[N]);
    }
}