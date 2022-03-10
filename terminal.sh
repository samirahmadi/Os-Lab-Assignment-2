:برای ایجاد یک دایرکتوری با استفاده از دستور زیر ابندا انرا میخوانیم
$ cd documents
result:~/Documents
:سپس با دستور زیر دایرکتوری را ایجاد میکنیم
$ mkdir test
برای ایجاد یک فایل در دایرکتوری موردنظر از دستورزیر 
mkdir -p
سپس  نام دایکتوری را با نام فایل جدید توسط / به ماشین منتقل میکنیم
$ mkdir -p test/t1
:و برای حذف دایرکتوری از دستور زیر استفاده میکنیم
$ rm -r test


whatt is: این دستور اطلاعاتی درمورد دایرکتوری مربوطی که به ان داده میشود را چاپ میکند

pwd:   این دستور اطلاعات مربوط به دایرکتوری ای که در همان لحظه در حال اجرا است را نشان میدهد.(print working directory)
1) - print name of current/working directory

rmdir:  این دستور دایرکتوری مربوط را در صورت خالی بودن  حذف میکند
1)remow empty directoreis
2)delete directory

find: در این دستور میتوانیم فایل های موردنظر را با اندازه فایل یا تاریخ ... \ییدا کرد
1) - search For files In a directory hierarch

stat: این دستور اطلاعاتی در مورد فایلها و سیستم فایل مانند: اندازه ی فایلها،شناسه فایلهاو.. در اختیار قرار میدهد
1) - display file or file system status 
2) - get file status

cat: این دستور به ما اجازه ی ایجاد چندفایل را میدهد و همچنین امکان تغییر مسیر خروجی فایلها(concatenate)
1) - concatenate files and print on the standard output

wc: با استفاده از این دستور میتوان تعداد خط ها، کلمه ها، کاراکترها رادر فایل  بشماریم(count)
1) - print newline, word, and byte counts For each file

