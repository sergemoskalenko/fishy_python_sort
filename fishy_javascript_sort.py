import time; R9=lambda s,c:int(abs((s:=int(s))^(s<<13)^(s>>17)^(s<<5))%c);ij=lambda a,s,i,j:(j,i)if(i:=R9(s,len(a)))>(j:=R9(s+731,len(a)))else(i,j); pr=lambda arr,src_arr: (print("\nSRC (in):", src_arr), print("\nWRK (out):", arr)); exec("def srt_f(arr): global seed; seed+=int(time.time()); i,j=ij(arr,seed,0,0); print(i, '<-->', j) if arr[i]>arr[j] else None; (arr[i],arr[j])=(arr[j],arr[i]) if arr[i]>arr[j] else (arr[i],arr[j]);\ndef shit_sort(arr, src_arr, t): [srt_f(arr) for _ in iter(lambda: not all(arr[i] <= arr[i+1] for i in range(len(arr) - 1)), False)];\nseed = int(time.time()); WRK = [int(R9(seed + i, 1000)) for i in range(100)]; SRC = WRK.copy(); print('\\nSorting WRK...'); shit_sort(WRK, SRC, True); pr(WRK, SRC);");
