local a=function(b,c)local d=string;local e=d.char;local f=d.byte;local g=d.sub;local h=d.reverse;local i=d.find;local j=function(k,l)local m,n=i(k,l)return m-c.a end;local o=function(...)local k=b.a;local p={...}for q=c.a,#p do k=k..p[q]end;return k end;local r=select;local s=table;local t=math;local u=error;local v=pairs;local w=ipairs;local x=s.concat;local y=s.insert;local z=function(...)return{}end;local A=s.unpack or unpack;local B=function(...)return{n=r(e(c.b),...),...}end;local C=function(D,E,F,G,H)for q=c.c,F-E do H[G+q]=D[E+q]end end;local I=function(...)local J={}local K={...}for q=c.a,#K do for L=c.a,#K[q]do y(J,K[q][L])end end;return J end;local M=getfenv;local N=t.floor;local O=t.max;local P=pcall;local Q=t.abs;local R=tonumber;local S=function(T,U,V)V=V or c.a;local W=U and T or c.a;U=U or T;local m={}for q=W,U,V do y(m,q)end;return m end;local X=function()local function Y(Z,...)if(Z or c.c)==c.c then return...end;return Y(N(Z/c.d),Z%c.d,...)end;local function _(Z)if Z==c.c then return{c.c}end;return{Y(Z)}end;local function _0(_1)local function _2(Z,_3,...)if not _3 then return Z end;Z,_3=_(Z),_(_3)local _4,_5=#Z,#_3;local _6,_7={},O(_4,_5)for q=c.c,_7-c.a do local _8,_9=Z[_4-q],_3[_5-q]if not(_8 or _9)then break end;_6[_7-q]=_1((_8 or c.c)~=c.c,(_9 or c.c)~=c.c)and c.a or c.c end;return _2(R(x(_6),c.d),...)end;return _2 end;local _a=_0(function(m,_b)return m and _b end)local function _c(Z,_d)return N(Z)*c.d^_d end;local function _e(Z,_d)return N(N(Z)/c.d^_d)end;return _a,_e,_c end;local _f,_g,_h=X()local _i;local _j;local _k;local function _l(D,_m,_n,_o)local _p=c.c;for q=_m,_n,_o do local _q=c.e^Q(q-_m)_p=_p+_q*f(D,q,q)end;return _p end;local function _r(_s,_t,_u,_v,_w,_x,_y,_z)local _A=(-c.a)^_g(_z,c.f)local _B=_h(_f(_z,c.g),c.h)+_g(_y,c.h)local _C=_f(_y,c.i)*c.d^c.j;local _D=c.a;_C=_C+_x*c.d^c.k+_w*c.d^c.l+_v*c.d^c.m+_u*c.d^c.n+_t*c.d^c.o+_s;if _B==c.c then if _C==c.c then return _A*c.c else _D=c.c;_B=c.a end elseif _B==c.p then if _C==c.c then return _A*c.a/c.c else return _A*c.c/c.c end end;return _A*c.d^(_B-c.q)*(_D+_C/c.d^c.r)end;local function _E(D,_m,_n)return _l(D,_m,_n-c.a,c.a)end;local function _F(D,_m)return _r(f(D,_m,_m+c.f))end;local function _G(_H)local _I=_H[c.a]local _J=f(_H[c.d],_I,_I)_H[c.a]=_I+c.a;return _J end;local function _K(_H,_L)local _M=_H[c.a]+_L;local k=g(_H[c.d],_H[c.a],_M-c.a)_H[c.a]=_M;return k end;local function _N(_H)local _M=_H[c.a]+c.d;local _O=_E(_H[c.d],_H[c.a],_M)_H[c.a]=_M;return _O end;local function _P(_H)local _M=_H[c.a]+c.h;local _O=_E(_H[c.d],_H[c.a],_M)_H[c.a]=_M;return _O end;local function _Q(_H)local _M=_H[c.a]+c.o;local _O=_E(_H[c.d],_H[c.a],_M)_H[c.a]=_M;return _O end;local function _R(_H)local _S=_F(_H[c.d],_H[c.a])_H[c.a]=_H[c.a]+c.o;return _S end;local function _T(_H)local _L=_Q(_H)local k;if _L~=c.c then k=g(_K(_H,_L),c.a,-c.d)end;return k end;local function _U(_H)local _L=_Q(_H)local _V=z(_L)for q=c.a,_L do local _W=_N(_H)local _X=_f(_g(_W,c.h),c.s)local _Y=_f(_g(_W,c.d),c.t)local _Z=_f(_g(_W,c.a),c.a)==c.a;local __=_f(_W,c.a)==c.a;local _00={}_00[c.u]=_X;_00[c.v]=_G(_H)if _Y==c.a then _00[c.i]=_N(_H)_00[c.f]=_N(_H)_00[c.w]=_Z and _00[c.i]>c.x;_00[c.n]=__ and _00[c.f]>c.x elseif _Y==c.d then _00[c.i]=_P(_H)_00[c.a]=_Z elseif _Y==c.t then _00[c.i]=_P(_H)-c.y end;_V[q]=_00 end;return _V end;local function _01(_H,D)local _L=_Q(_H)local _V=z(_L)for q=c.a,_L do _V[q]=_k(_H,D)end;return _V end;local function _02(_H)local _L=_Q(_H)local _V=z(_L)for q=c.a,_L do local _03=_G(_H)local _04;if _03==c.d then _04=_G(_H)~=c.c elseif _03==c.c then _04=_R(_H)elseif _03==c.a then _04=_T(_H)end;_V[q]=_04 end;return _V end;function _k(_05,_06)local D=_T(_05)or _06;local _07={}_07[c.z]=D;_07[c.o]=_G(_05)_07[c.ab]=_G(_05)_07[c.d]=_02(_05)_07[c.h]=_01(_05,D)_07[c.bb]=_U(_05)for n,_08 in w(_07[c.bb])do if _08[c.a]then _08[c.cb]=_07[c.d][_08[c.i]+c.a]else if _08[c.w]then _08[c.db]=_07[c.d][_08[c.i]-c.x]end;if _08[c.n]then _08[c.t]=_07[c.d][_08[c.f]-c.x]end end end;return _07 end;function _i(D)local _05={c.a,D}return _k(_05,b.a)end;local function _09(_V,_0a)for q,_0b in v(_V)do if _0b[c.a]>=_0a then _V[q]=nil end end end;local function _0c(_V,_0a,_0d)local _0e=_V[_0a]if not _0e then _0e={_0a,_0d}_V[_0a]=_0e end;return _0e end;local function _0f(_0g,_0h)local D=_0g[c.d]local _0i=c.c;u(o(D,b.b,_0i,b.b,_0h),c.c)end;local function _0j(_0k,_0l,_0m)local _0n=_0k[c.t]local _0o=_0k[c.h]local _0p=_0k[c.a]local _0q=-c.a;local _0r={}local _0d=_0k[c.d]local _0s=_0k[c.w]local function _0t(_0u)return _0u[c.w]and _0u[c.db]or _0d[_0u[c.i]]end;local function _0v(_0u)return _0u[c.n]and _0u[c.t]or _0d[_0u[c.f]]end;while true do local _0u=_0n[_0s]local _X=_0u[c.u]_0s=_0s+c.a;if _X==c.c then _0d[_0u[c.v]]=_0d[_0u[c.i]]elseif _X==c.a then _0d[_0u[c.v]]=_0u[c.cb]elseif _X==c.d then _0d[_0u[c.v]]=_0u[c.i]~=c.c;if _0u[c.f]~=c.c then _0s=_0s+c.a end elseif _X==c.t then local _0w=_0o[_0u[c.i]+c.a]local _0x=_0w[c.o]local _0y;if _0x~=c.c then _0y={}for q=c.a,_0x do local _0z=_0n[_0s+q-c.a]if _0z[c.u]==c.c then _0y[q-c.a]=_0c(_0r,_0z[c.i],_0d)end end;_0s=_0s+_0x end;_0d[_0u[c.v]]=_j(_0w,_0l,_0y)elseif _X==c.h then local _0A=_0u[c.v]local _0B=_0u[c.i]local _0C=_0u[c.f]local _0D;if _0B==c.c then _0D=_0q-_0A else _0D=_0B-c.a end;local _0E=B(_0d[_0A](A(_0d,_0A+c.a,_0A+_0D)))local _0F=_0E.n;if _0C==c.c then _0q=_0A+_0F-c.a else _0F=_0C-c.a end;C(_0E,c.a,_0F,_0A,_0d)elseif _X==c.w then _0s=_0s+_0u[c.i]elseif _X==c.v then local _0A=_0u[c.v]local _0B=_0u[c.i]local _L;if _0B==c.c then _L=_0q-_0A+c.a else _L=_0B-c.a end;_09(_0r,c.c)return A(_0d,_0A,_0A+_L-c.a)elseif _X==c.f then if not _0d[_0u[c.v]]~=(_0u[c.f]~=c.c)then _0s=_0s+_0n[_0s][c.i]end;_0s=_0s+c.a elseif _X==c.o then _0d[_0u[c.v]]=_0l[_0u[c.cb]]elseif _X==c.ab then _0d[_0u[c.v]]=_0d[_0u[c.i]][_0v(_0u)]end;_0k[c.w]=_0s end end;function _j(_07,_0l,_0G)_0l=_0l or M(c.c)local function _0H(...)local _0I=B(...)local _0d=z()local _0p={c.c,{}}C(_0I,c.a,_07[c.ab],c.c,_0d)if _07[c.ab]<_0I.n then local W=_07[c.ab]+c.a;local _L=_0I.n-_07[c.ab]_0p[c.a]=_L;C(_0I,W,W+_L-c.a,c.a,_0p[c.d])end;local _0k={_0p,_0d,_07[c.bb],_07[c.h],c.a}local _0J=B(P(_0j,_0k,_0l,_0G))if _0J[c.a]then return A(_0J,c.d,_0J.n)else local _0g={_0k[c.w],_07[c.z]}_0f(_0g,_0J[c.d])return end end;return _0H end;local _0K=e(A(I(S(c.j,c.eb),S(c.fb,c.gb))))local function _0L(_0M)local _p,k=c.c,h(_0M)for q=c.a,#k do _p=_p+j(_0K,g(k,q,q))*c.hb^(q-c.a)end;return _p end;local function _0N(_0O)local _0P,_0Q,_0R,_0S,_04={},c.e,b.a,e(_0O[c.a])local _0J={_0S}for q=c.c,c.x do _0P[q]=e(q)end;for q=c.d,#_0O do _04=_0O[q]if _0P[_04]then _0R=_0P[_04]elseif _04==_0Q then _0R=_0S..g(_0S,c.a,c.a)else return nil,q end;y(_0J,_0R)_0P[_0Q]=_0S..g(_0R,c.a,c.a)_0Q=_0Q+c.a;_0S=_0R end;return x(_0J)end;local function _0T(_0U)local _0V={}local q=c.a;while q<=#_0U do local _L=_0L(g(_0U,q,q))q=q+c.a;y(_0V,_0L(g(_0U,q,q+_L-c.a)))q=q+_L end;return _0N(_0V)end;_j(_i(_0T(b.c)))()end;a({a=[[]],b=[[:]],c=[[1B102752761021S23822T23123421E21A23023922P27727J2751127K27N2771527O27K21421S111627N23423622X23223810111727N23723827Z23222V28328527K22U23323623122P282111K27N22022T2302302331W22F28G23022S1X1W23A21D21M1W21122S27R1C27N1Q27K21028327M27528K27722K27527W121023U101229D29L101329K27524529R1329R1129914142762A227Q27621W29W2A629N27L1029528327629T27J21K27K2AD29P]]},{a=1,b=35,c=0,d=2,e=256,f=7,g=127,h=4,i=15,j=48,k=40,l=32,m=24,n=16,o=8,p=2047,q=1023,r=52,s=63,t=3,u=12,v=6,w=5,x=255,y=131071,z=17,ab=9,bb=13,cb=11,db=10,eb=57,fb=65,gb=90,hb=36})