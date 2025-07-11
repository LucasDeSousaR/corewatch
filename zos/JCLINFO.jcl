//JOBNAME  JOB (ACCT),'DESCRIPTION',CLASS=A,MSGCLASS=X,NOTIFY=&SYSUID
//STEP1    EXEC PGM=IEFBR14
//SYSOUT   DD SYSOUT=*
//*
//* Captura o nome da LPAR
//GETLPAR  EXEC PGM=IKJEFT01,REGION=0M
//SYSTSPRT DD SYSOUT=*
//SYSTSIN  DD *
  D IPLINFO
/*
//*
//* Captura o consumo de CPU da LPAR atual
//GETCPU   EXEC PGM=RMF,PARM='REPORTS(CPU)'
/*
//*
//* Captura o IPV4 da LPAR
//GETIPV4  EXEC PGM=IKJEFT01,REGION=0M
//SYSTSPRT DD SYSOUT=*
//SYSTSIN  DD *
  D TCPIP,,NETSTAT HOME
/*
//*
//* Captura o LUNAME da LPAR
//GETLUNAM EXEC PGM=IKJEFT01,REGION=0M
//SYSTSPRT DD SYSOUT=*
//SYSTSIN  DD *
  D NET,ID=LU
/*
//*
//* Captura o valor dos MSUs
//GETMSU   EXEC PGM=IEEEMC00
//SYSPRINT DD SYSOUT=*
//SYSIN    DD *
  DISPLAY M=CPU
/*
//*
//* Verifica a disponibilidade do SMF
//GETSMF   EXEC PGM=IKJEFT01,REGION=0M
//SYSTSPRT DD SYSOUT=*
//SYSTSIN  DD *
  D SMF
/*