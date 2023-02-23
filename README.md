# RemoveFalsePositives
As we all know, Usage of syscall stub: `\x4c\x8b\xd1\xb8` to detect Hooked NtApis creates False Positive results.\
To erradicate that while **performing Dynamic EDR Evasion**, we can use this Scipt (seeing the Demo Video, before using it will be useful!)

### Usage:
```
$ python3 GetFalsePositiveHooks.py <FalsePositiveHooks.txt>
```

### This can be used along with my previous project: _<ins>[CheckHooks-n-load](https://github.com/reveng007/CheckHooks-n-load)</ins>_.

### Target of this small python script:

https://user-images.githubusercontent.com/61424547/220876716-c600844b-12e3-4218-a1a9-007233b63c2a.mp4

Video link: https://drive.google.com/file/d/1s52YLW4DC8b4T8t9z4aEdQQvdtticpTY/view?usp=share_link
