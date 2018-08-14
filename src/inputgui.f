c inputgui.f
c generate structure files from raw pdb files
c m. peters march 20, 2013
c
c       character(len=1) :: chida,chidb
c
c       chida="A"
c       chidb="B"
c
c       call inpututil(chida,chidb)
c       end
c
c       subroutine inpututil()
c
c       module inputgui
c
c       contains
c
       subroutine inpututil(chida,chidb)
c
       implicit real(a-h,o-z)
       integer resnr,nbar,ljnbar,ljrsnr
       integer resns,nbars
       integer resnc,nbarc
       integer resnn,nbarn
c
       integer numa,numb,ns,n
c
       character*6 card,cards,cardc,cardn,ljcard
c
       character*1 alt,ljalt,chid,ljchid,code,ljcode
       character*1 alts,chids,codes
       character*1 altc,chidc,codec
       character*1 altn,chidn,coden
       character*1 chida,chidb
c
       character*4 atomna,ljatna
       character*4 atomns
       character*4 atomnc
       character*4 atomnn
c
       character*3 resna,ljrsna
       character*3 resnas
       character*3 resnac
       character*3 resnan
c
       open(unit=1, file='prota.pdb', status='old')
       open(unit=2, file='protb.pdb', status='old')
c       open(unit=14, file='chaina', status='old')
c       open(unit=15, file='chainb', status='old')
       open(unit=3, file='ljresid', status='old')
       open(unit=4, file='residc03.pdb', status='old')
c
c terminal residue files
       open(unit=5, file='ntresc03.pdb', status='old')
       open(unit=6, file='ctresc03.pdb', status='old')
c
       open(unit=7, file='proteina', status='new')
       open(unit=8, file='proteinb', status='new')
       open(unit=9, file='lja', status='new')
       open(unit=10, file='ljb', status='new')
       open(unit=11, file='atnma', status='new')
       open(unit=12, file='atnmb', status='new')
c
c number of atoms in residue files
       matom=435
       mct=455
       mnt=523
       mlj=550
c
       mres=23
c
c read protein A raw pdb file
c
       rewind(1)
       rewind(2)
c       rewind(14)
c       rewind(15)
c
       numa=0
       numb=0      
c
c trim string (trim command removes trailing spaces)
c        chida=trim(adjustl(chida))
c        chidb=trim(adjustl(chidb))
c
c       read(unit=14,fmt=16)chida
c       read(unit=15,fmt=16)chidb
c 16    format(a1)
c
 80    read(unit=1,fmt=10,end=99,iostat=ios)card,nbar,atomna,alt,resna,
     1     chid,resnr,
     1     code,x,y,z
 10    format(a6,i5,1x,a4,a1,a3,1x,a1,i4,a1,3x,3f8.3)
c
c parse unwanted lines
       if(ios==0.and.(card.eq."ATOM  ".or.card.eq."HETATM"))then
c make this one protein A
       if(chid.eq.chida)then
c
       rewind(3)
       rewind(4)
       rewind(5)
       rewind(6)
c      
       do 19 j=1,matom
       read(unit=4,fmt=12)cards,nbars,atomns,alts,resnas,chids,resns,
     1     codes,xs,ys,zs,amass,acharge
 12    format(a6,i5,1x,a4,a1,a3,1x,a1,i4,a1,3x,5f8.3)
c
       if(resna.eq.resnas.and.atomna.eq.atomns)then
       write(unit=7,fmt=12)card,nbar,atomna,alt,resna,chid,resnr,
     1     code,x,y,z,amass,acharge
       numa=numa+1
       end if
c
 19    continue
c
c check for cterm oxt
c
       if(atomna.eq." OXT")then
c
       do 20 j=1,mct
       read(unit=6,fmt=12)cardc,nbarc,atomnc,altc,resnac,chidc,resnc,
     1     codec,xc,yc,zc,amass,acharge
c
       if(resna.eq.resnac.and.atomna.eq.atomnc)then
       write(unit=7,fmt=12)card,nbar,atomna,alt,resna,chid,resnr,
     1     code,x,y,z,amass,acharge
       numa=numa+1
       end if
c
 20    continue
c
       end if
c
c check for nterm ht1 or ht2
c
       if(atomna.eq." HT1".or.atomna.eq." HT2")then
c
       do 21 j=1,mnt
       read(unit=5,fmt=12)cardn,nbarn,atomnn,altn,resnan,chidn,resnn,
     1     coden,xn,yn,zn,amass,acharge
c
       if(resna.eq.resnan.and.atomna.eq.atomnn)then
       write(unit=7,fmt=12)card,nbar,atomna,alt,resna,chid,resnr,
     1     code,x,y,z,amass,acharge
       numa=numa+1
       end if
 21   continue
c
       end if
c
c end chid loop
       end if
c end parsing
       end if
c
       go to 80
c
 99    write(unit=11,fmt=14)numa
 14    format(i6)
c
c now add lj constants to file
c
       rewind(7)
c
       do 30 k=1,numa
       read(unit=7,fmt=12)card,nbar,atomna,alt,resna,chid,resnr,
     1     code,x,y,z,amass,acharge
c
       do 31 l=1,mlj
       read(unit=3,fmt=6)ljcard,ljnbar,ljatna,ljalt,ljrsna,ljchid,
     1     ljrsnr,ljcode,siglj,epslj
 6     format(a6,i5,1x,a4,a1,a3,1x,a1,i4,a1,1x,2f9.5) 
c      
       if(ljrsna.eq.resna.and.ljatna.eq.atomna)then
       write(unit=9,fmt=6)card,nbar,atomna,alt,resna,chid,resnr,
     1     code,siglj,epslj
       end if

 31    continue
       rewind(3)
c
 30    continue
c
c read protein b
c
 81    read(unit=2,fmt=10,end=98,iostat=ios)card,nbar,atomna,alt,resna,
     1     chid,resnr,
     1     code,x,y,z
c
c parse unwanted lines
       if(ios==0.and.(card.eq."ATOM  ".or.card.eq."HETATM"))then
c make this protein B
       if(chid.eq.chidb)then
c
       rewind(3)
       rewind(4)
       rewind(5)
       rewind(6)
c      
       do 22 j=1,matom
       read(unit=4,fmt=12)cards,nbars,atomns,alts,resnas,chids,resns,
     1     codes,xs,ys,zs,amass,acharge
c
       if(resna.eq.resnas.and.atomna.eq.atomns)then
       write(unit=8,fmt=12)card,nbar,atomna,alt,resna,chid,resnr,
     1     code,x,y,z,amass,acharge
       numb=numb+1
       end if
c
 22    continue
c
       if(atomna.eq." OXT")then
c
       do 23 j=1,mct
       read(unit=6,fmt=12)cardc,nbarc,atomnc,altc,resnac,chidc,resnc,
     1     codec,xc,yc,zc,amass,acharge
c
       if(resna.eq.resnac.and.atomna.eq.atomnc)then
       write(unit=8,fmt=12)card,nbar,atomna,alt,resna,chid,resnr,
     1     code,x,y,z,amass,acharge
       numb=numb+1
       end if
c
 23    continue
c
       end if
c
       if(atomna.eq." HT1".or.atomna.eq." HT2")then
c
       do 24 j=1,mnt
       read(unit=5,fmt=12)cardn,nbarn,atomnn,altn,resnan,chidn,resnn,
     1     coden,xn,yn,zn,amass,acharge
c
       if(resna.eq.resnan.and.atomna.eq.atomnn)then
       write(unit=8,fmt=12)card,nbar,atomna,alt,resna,chid,resnr,
     1     code,x,y,z,amass,acharge
       numb=numb+1
       end if
 24   continue
c
       end if
c
c end chid loop
       end if
c end parsing
       end if
c
       go to 81
c
 98    write(unit=12,fmt=14)numb
c
c now add lj constants to file
c
       rewind(8)
c
       do 32 k=1,numb
       read(unit=8,fmt=12)card,nbar,atomna,alt,resna,chid,resnr,
     1     code,x,y,z,amass,acharge
c
       do 33 l=1,mlj
       read(unit=3,fmt=6)ljcard,ljnbar,ljatna,ljalt,ljrsna,ljchid,
     1     ljrsnr,ljcode,siglj,epslj
c      
       if(ljrsna.eq.resna.and.ljatna.eq.atomna)then
       write(unit=10,fmt=6)card,nbar,atomna,alt,resna,chid,resnr,
     1     code,siglj,epslj
       end if

 33    continue
       rewind(3)
c
 32    continue
c
       close(1)
       close(2)
       close(3)
       close(4)
       close(5)
       close(6)
       close(7)
       close(8)
       close(9)
       close(10)
       close(11)
       close(12)
c       close(14)
c       close(15)
c 
       end subroutine inpututil
c      
c       end module inputgui
c









