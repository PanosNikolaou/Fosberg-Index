from math import sqrt

humidity = 70.0
temperature = 14.0
windspeed = 10.0

T = float(temperature)
H = float(float(humidity)/100)
W = 349 + (1.29*T)+(0.0135*(T**2))
K = 0.805 + 0.000736*T - 0.000000273*(T**2)
K1 = 6.27 + 0.000938*T - 0.0000303*(T**2)
K2 = 1.91 + 0.0407*T - 0.000293*(T**2)
M = 1800/W *(((K*H)/(1-(K*H)))+(((K1*K*H)+(2*K1*K2*(K**2)*(H**2)))/(1+(K1*K*H)+(K1*K2*(K**2)*(H**2)))))
        
WMPH = float(windspeed)
        
M30 = M/30
WSQR = WMPH*WMPH
fmdc = 1 - 2*M30 + 1.5*M30**2 - 0.5*M30**3
CMBE = (fmdc*sqrt(1+WSQR))/0.3002
ffwi = str(round(CMBE,0))
print(ffwi)