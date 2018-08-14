c	contactgui.f 
c       by m. h. peters - jan 2, 2013
c
c 30000 protein a atoms, 30000 protein b atoms
c
c        call contact()
c        end
c
        subroutine contact()
c
        real xa(30000),ya(30000),za(30000),
     1       amsa(30000),charga(30000)
        real xb(30000),yb(30000),zb(30000),amsb(30000),chargb(30000)
        real sigma(30000),epsla(30000),sigmb(30000),epslb(30000)
        integer resnr,nbar,na,nb,resnra,resnrb,nbara,nbarb
        integer atnuma(30000),atnumb(30000),isava(30000),isavb(30000),
     1       resnma(30000),resnmb(30000),ifsava(30000),ifsavb(30000)
        character*6 card,ljcard,carda,cardb
        character*1 alt,ljalt,chid,ljchid,code,ljcode
        character*1 alta,chida,codea
        character*1 altb,chidb,codeb
        character*4 atomna,ljatna,atnama(30000),atnamb(30000)
        character*4 atmnaa,atmnab
        character*3 resna,ljrsna,resa(30000),resb(30000),resnaa,resnab
c
c open protein atomic coordinates
c note all input quantities should carry dimensions (MKS system)
c since this program conducts its own scaling 
c
        open(unit=1, file='proteina', status='old')
        open(unit=2, file='proteinb', status='old')
        open(unit=3, file='atnma', status='old')
        open(unit=4, file='atnmb', status='old')
        open(unit=5, file='lja', status='old')
        open(unit=6, file='ljb', status='old')
c
        open(unit=7, file='finea.pdb', status='new')
        open(unit=8, file='fineb.pdb', status='new')
        open(unit=9, file='fineab.pdb', status='new')
        open(unit=10, file='coarsea.pdb', status='new')
        open(unit=11, file='coarseb.pdb', status='new')
        open(unit=12, file='coarseab.pdb', status='new')
        open(unit=14, file='coarsedata.txt', status='new')
        open(unit=15, file='finedata.txt', status='new')
        open(unit=20, file='unsortc.pdb', status='new')
        open(unit=21, file='unsortf.pdb', status='new')
c
c scaling variables (kg, m ,s, K)
c mass scaling below corresponds to about 50 carbon atoms 
c length scaling is 1 nanometers; rmu is water viscosity at 310K
        xo=1.0e-09
        rm=1.35e-25
        rk=1.38048e-23
        temp=310.15
        fcoul=53.936
        epsw=80.0
        caps=0.50e+10
        pi=3.1415297
c
c sig is an average atomic diameter used for LJ potential cut-off
        sigavg=3.0e-10
        rlamax=3.5*sigavg
c
c echo input values and scaling quantities
       write(18,101)xo,rm,rk,temp,fcoul,epsw,caps
 101   format('dimensional input values',/'xo rm rk',/,3e15.8,/,
     1 'temp fcoul epsw caps',/,4e15.8,/)
c
       rewind(1)
       rewind(2)
       rewind(3)
       rewind(4)
       rewind(5)
       rewind(6)

       read(unit=3,fmt=12)na
 12    format(i6)
       write(18,205)na
 205   format('number of protein A atoms',i6)
c
       read(unit=4,fmt=12)nb
       write(18,206)nb
 206   format('number of protein B atoms',i6)
c
c read protein A atomic coordinates
c
       do 9 i=1,na
       read(unit=1,fmt=10)card,nbar,atomna,alt,resna,chid,resnr,
     1     code,xl,yl,zl,amass,acharge
 10    format(a6,i5,1x,a4,a1,a3,1x,a1,i4,a1,3x,5f8.3)
       xa(i)=xl
       ya(i)=yl
       za(i)=zl
       amsa(i)=amass
       resa(i)=resna
       resnma(i)=resnr
       charga(i)=acharge
       atnama(i)=atomna
       atnuma(i)=nbar
c echo for check
c       write(19,102)card,nbar,atnama(i),alt,resa(i),chid,resnr,code,
c     1     xa(i),ya(i),za(i),amsa(i),chargb(i)
c 102   format(a6,i5,1x,a4,a1,a3,1x,a1,i4,a1,3x,5f8.3)                    
 9     continue
c
c read protein b atomic coordinates
       do 11 i=1,nb
       read(unit=2,fmt=10)card,nbar,atomna,alt,resna,chid,resnr,
     1     code,xr,yr,zr,amass,acharge
       xb(i)=xr
       yb(i)=yr
       zb(i)=zr
       amsb(i)=amass
       resb(i)=resna
       resnmb(i)=resnr
       chargb(i)=acharge
       atnamb(i)=atomna
       atnumb(i)=nbar
c echo for check
c       write(19,102)card,nbar,atnamb(i),alt,resb(i),chid,resnr,code,
c     1     xb(i),yb(i),zb(i),amsb(i),chargb(i)
 11    continue
c
c read in lj constants for protein a and b 
c sig is in nm and eps is in kJ/mole
c
c protein A
c
       do 8 i=1,na
       read(unit=5,fmt=6)card,nbar,atomna,alt,resna,chid,resnr,
     1     code,siglj,epslj
 6     format(a6,i5,1x,a4,a1,a3,1x,a1,i4,a1,1x,2f9.5)
c convert to program units and nondimensionalize
       sigma(i)=siglj
       epsla(i)=0.387967*epslj
c echo sigs and epss for check
c       write(18,103)sigma(i),epsla(i)
c 103   format(2e15.8)
 8     continue
c
c protein B
c
       do 7 i=1,nb
       read(unit=6,fmt=6)card,nbar,atomna,alt,resna,chid,resnr,
     1     code,siglj,epslj
c convert to program units and nondimensionalize
       sigmb(i)=siglj
       epslb(i)=0.387967*epslj
c echo sig and eps for check
c       write(18,103)sigmb(i),epslb(i)
 7     continue
c
c convert to program units (meters) and scale
       rlamax=rlamax/xo
       caps=caps*xo
       do 24 j=1,na
       xa(j)=xa(j)*1.0e-10/xo
       ya(j)=ya(j)*1.0e-10/xo
       za(j)=za(j)*1.0e-10/xo
 24    continue
       do 23 i=1,nb
       xb(i)=xb(i)*1.0e-10/xo
       yb(i)=yb(i)*1.0e-10/xo
       zb(i)=zb(i)*1.0e-10/xo
 23    continue
c
c initialize forces, torques, and total potential 
       fx=0.0
       fy=0.0
       fz=0.0
       tx=0.0
       ty=0.0
       tz=0.0
       us=0.0
c
c now compute the force acting on protein A 
c
       icoura=0
       icourb=0
       ifina=0
       ifinb=0
       icontact=0
       rewind(1)
c
       do 27 j=1,na
       read(unit=1,fmt=10)carda,nbara,atmnaa,alta,resnaa,chida,resnra,
     1     codea,xla,yla,zla,amassa,achargea
       xaj=xa(j)
       yaj=ya(j)
       zaj=za(j)
c
       rewind(2)
       do 28 i=1,nb
       read(unit=2,fmt=10)cardb,nbarb,atmnab,altb,resnab,chidb,resnrb,
     1     codeb,xlb,ylb,zlb,amassb,achargeb
       xxs=xaj-xb(i)
       yys=yaj-yb(i)
       zzs=zaj-zb(i)
       rrs=sqrt(xxs*xxs+yys*yys+zzs*zzs)
c simple lennard jones potential
c
       epsab=(epsla(j)*epslb(i))**0.5
       sigmab=(sigma(j)+sigmb(i))/2.0
       c6a=4.0*epsab*sigmab**6.0
       c12a=4.0*epsab*sigmab**12.0
c
c avoid large values for overlapping atoms
       sigmp=0.9*sigmab
       if(rrs.lt.sigmp)then
       rrs=sigmp
       end if
c
c also don't include very large separation distances in the contact map
       if (rrs.gt.rlamax)go to 28
c
       rs148=12.0*c12a*rrs**(-14.0)-6.0*c6a*rrs**(-8.0)
       us148=c12a*rrs**(-12.0)-c6a*rrs**(-6.0)
c
       epseff=epsw-(((epsw-1.0)/2.0)*((rrs*caps)**2+2.0*rrs*caps+2.0)
     1                *exp(-(rrs*caps)))
       couls=chargb(i)*charga(j)*(fcoul/epseff)*(1.0/(rrs**3))
       ucouls=couls*(rrs**2)
c
       rs148c=rs148+couls
       us148c=us148+ucouls
c
       fx=fx+xxs*rs148c
       fy=fy+yys*rs148c
       fz=fz+zzs*rs148c
       tx=tx+yspj*zzs*rs148c-zspj*yys*rs148c
       ty=ty+zspj*xxs*rs148c-xspj*zzs*rs148c
       tz=tz+xspj*yys*rs148c-yspj*xxs*rs148c
c
c net interaction potential and total contacts
       us=us+us148c
       icontact=icontact+1
c
c coarse contact map data
c
       write(unit=14,fmt=126)resa(j),resnma(j),atnama(j),atnuma(j),
     1                      resb(i),resnmb(i),atnamb(i),atnumb(i),
     1                      rrs,ucouls,us148
 126   format(a3,i6,a4,i6,1x,a3,i6,a4,i6,2x,e10.3,2x,
     1     e10.3,2x,e10.3)
c
c fine contact map data
c
       if(ucouls.lt.-0.3.or.us148.lt.-0.1)then
c
       ifine=2
       write(unit=15,fmt=126)resa(j),resnma(j),atnama(j),atnuma(j),
     1                      resb(i),resnmb(i),atnamb(i),atnumb(i),
     1                      rrs,ucouls,us148
c
c write fine contact map for matplotlib
c
       write(16,127)resa(j),',',resnma(j),',',atnama(j),',',
     1                      atnuma(j),',', resb(i),',',resnmb(i),',',
     1                      atnamb(i),',',atnumb(i),',',
     1                      rrs,',',us148,',',ucouls
 127   format(a3,a1,i6,a1,a4,a1,i6,a1,a3,a1,i6,a1,a4,a1,i6,a1,e15.8,a1,
     1                      e15.8,a1,e15.8)
c
c print for matlab program
c       write(26,129)atnuma(j),atnumb(i),
c     1                      rrs,ucouls,us148
c 129   format(i6,2x,i6,2x,e15.8,2x,e15.8,2x,e15.8)
c
       else
       ifine=1
       end if
c
c save filtered pdb's - these have duplicate atoms and same number of lines
c
       write(unit=10,fmt=10)carda,nbara,atmnaa,alta,resnaa,chida,resnra,
     1     codea,xla,yla,zla,amassa,achargea
       if(ifine.eq.2)then
       write(unit=7,fmt=10)carda,nbara,atmnaa,alta,resnaa,chida,resnra,
     1     codea,xla,yla,zla,amassa,achargea
       ifina=ifina+1
       end if
       icoura=icoura+1
c
       write(unit=20,fmt=10)cardb,nbarb,atmnab,altb,resnab,chidb,resnrb,
     1     codeb,xlb,ylb,zlb,amassb,achargeb
       if(ifine.eq.2)then
       write(unit=21,fmt=10)cardb,nbarb,atmnab,altb,resnab,chidb,resnrb,
     1     codeb,xlb,ylb,zlb,amassb,achargeb
       ifinb=ifinb+1
       end if
       icourb=icourb+1
c
 28    continue
c
 27    continue
c
c print total number of contacts and total interaction potential (coarse)
       usbar=us/real(icontact)
c       write(30,130)icontact,us,usbar
c 130   format(i6,2x,e15.8,2x,e15.8)
c
c sort B chain pdb in proper order for visualization
c
       rewind(2)
c 
       do 31 i=1,nb
       read(unit=2,fmt=10)card,nbar,atomna,alt,resna,chid,resnr,
     1     code,xr,yr,zr,amass,acharge
c
       rewind(20)
       do 32 j=1,icourb
       read(unit=20,fmt=10)cardb,nbarb,atmnab,altb,resnab,chidb,resnrb,
     1     codeb,xlb,ylb,zlb,amassb,achargeb
       if(nbarb.eq.nbar)then
       write(unit=11,fmt=10)card,nbar,atomna,alt,resna,chid,resnr,
     1     code,xr,yr,zr,amass,acharge 
       end if
 32    continue
c
       rewind(21)
       do 33 j=1,ifinb
       read(unit=21,fmt=10)cardb,nbarb,atmnab,altb,resnab,chidb,resnrb,
     1     codeb,xlb,ylb,zlb,amassb,achargeb
       if(nbarb.eq.nbar)then
       write(unit=8,fmt=10)card,nbar,atomna,alt,resna,chid,resnr,
     1     code,xr,yr,zr,amass,acharge 
       end if
 33   continue
c
 31   continue
c
c combine filtered pdb's into one file and remove duplicate atoms
       rewind(7)
       rewind(8)
       rewind(10)
       rewind(11)
c
       do 37 j=1,icoura
       read(unit=10,fmt=10)carda,nbara,atmnaa,alta,resnaa,chida,resnra,
     1     codea,xla,yla,zla,amassa,achargea
c save this atom number
       isava(j)=nbara
       if(j.eq.1)then
       write(unit=12,fmt=10)carda,nbara,atmnaa,alta,resnaa,chida,resnra,
     1     codea,xla,yla,zla,amassa,achargea
       else
c if it appeared once before then don't write it
       icodea=1
       jm1=j-1
       do 41 k=1,jm1
       if(nbara.eq.isava(k))icodea=2
 41    continue
       if(icodea.eq.1)then
       write(unit=12,fmt=10)carda,nbara,atmnaa,alta,resnaa,chida,resnra,
     1     codea,xla,yla,zla,amassa,achargea
       end if
       end if
 37    continue
c
       do 38 i=1,icourb
       read(unit=11,fmt=10)cardb,nbarb,atmnab,altb,resnab,chidb,resnrb,
     1     codeb,xlb,ylb,zlb,amassb,achargeb
       isavb(i)=nbarb
       if(i.eq.1)then
       write(unit=12,fmt=10)cardb,nbarb,atmnab,altb,resnab,chidb,resnrb,
     1     codeb,xlb,ylb,zlb,amassb,achargeb
       else
       icodeb=1
       im1=i-1
       do 42 k=1,im1
       if(nbarb.eq.isavb(k))icodeb=2
 42    continue
       if(icodeb.eq.1)then
       write(unit=12,fmt=10)cardb,nbarb,atmnab,altb,resnab,chidb,resnrb,
     1     codeb,xlb,ylb,zlb,amassb,achargeb
       end if
       end if
 38    continue
c
       do 39 j=1,ifina
       read(unit=7,fmt=10)carda,nbara,atmnaa,alta,resnaa,chida,resnra,
     1     codea,xla,yla,zla,amassa,achargea
       ifsava(j)=nbara
       if(j.eq.1)then
       write(unit=9,fmt=10)carda,nbara,atmnaa,alta,resnaa,chida,resnra,
     1     codea,xla,yla,zla,amassa,achargea
       else
       icodea=1
       jm1=j-1
       do 43 k=1,jm1
       if(nbara.eq.ifsava(k))icodea=2
 43    continue
       if(icodea.eq.1)then
       write(unit=9,fmt=10)carda,nbara,atmnaa,alta,resnaa,chida,resnra,
     1     codea,xla,yla,zla,amassa,achargea
       end if
       end if
 39    continue
c
       do 40 i=1,ifinb
       read(unit=8,fmt=10)cardb,nbarb,atmnab,altb,resnab,chidb,resnrb,
     1     codeb,xlb,ylb,zlb,amassb,achargeb
       ifsavb(i)=nbarb
       if(i.eq.1)then
       write(unit=9,fmt=10)cardb,nbarb,atmnab,altb,resnab,chidb,resnrb,
     1     codeb,xlb,ylb,zlb,amassb,achargeb
       else
       icodeb=1
       im1=i-1
       do 44 k=1,im1
       if(nbarb.eq.ifsavb(k))icodeb=2
 44    continue
       if(icodeb.eq.1)then
       write(unit=9,fmt=10)cardb,nbarb,atmnab,altb,resnab,chidb,resnrb,
     1     codeb,xlb,ylb,zlb,amassb,achargeb
       end if
       end if  
 40    continue
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
       close(14)
       close(15)
       close(18)
       close(19)
       close(unit=20, status='delete')
       close(unit=21, status='delete')
c
        return
        end
