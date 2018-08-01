%us148plot.m
load fort26
%
n1=fort26(:,1);
m1=fort26(:,2);
z1=fort26(:,4);
%
scatter3(n1(:),m1(:),z1(:), 10, z1(:))
colormap(hsv)
view(40,40)
colorbar
%plot3(n1,m1,z1,'o')
grid on
xlabel('Prot A-ATM NUM-DomainIV')
ylabel('Prot B-ATM NUM-DomainII')
zlabel('ULJ148 (dimensionless via kT)')
title('Lennard-Jones Potential Plot')

