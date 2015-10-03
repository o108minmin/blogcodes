import math
from enum import Enum

class roundmode(Enum):
    up=1
    nearest=0
    down=-1

class roundfloat:
    def split(floatArg):
        tmp=floatArg*(2**27+1)
        x=tmp-(tmp-floatArg)
        y=floatArg-x
        return x,y

    def succ(floatArg):
        a=abs(floatArg)
        if a >= 2.**(-969):
            return floatArg+a*(2.**(-53)+2.**(-105))
        if a< 2.**(-1021):
            return floatArg+a*2.**(-1074)
        c=2.**(53)*floatArg
        e=(2.**(-53)+2.**(-105))*abs(c)
        return (c+e)*2.**(-53)

    def pred(floatArg):
        a=abs(floatArg)
        if a >= 2.**(-969):
            return floatArg-a*(2.**(-53)+2.**(-105))
        if a< 2.**(-1021):
            return floatArg-a*2.**(-1074)
        c=2.**(53)*floatArg
        e=(2.**(-53)+2.**(-105))*abs(c)
        return (c-e)*2.**(-53)

    def twosum(floatArg1,floatArg2):
        x=floatArg1 + floatArg2
        if abs(floatArg1)>abs(floatArg2):
            tmp=x-floatArg1
            y=floatArg2-tmp
        else:
            tmp=x-floatArg2
            y=floatArg1-tmp
        return x,y

    def twoproduct(floatArg1,floatArg2):
        x=floatArg1*floatArg2
        if abs(floatArg1) > 2.**996:
            floatArg1fix=floatArg1*2.**(-28)
            floatArg2fix=floatArg2*2.**(28)
        elif abs(floatArg2) > 2.**(996):
            floatArg1fix=floatArg1*2.**(28)
            floatArg2fix=floatArg2*2.**(-28)
        else:
            floatArg1fix=floatArg1
            floatArg2fix=floatArg2
        floatArg1SplitUp,floatArg1SplitDown=roundfloat.split(floatArg1fix)
        floatArg2SplitUp,floatArg2SplitDown=roundfloat.split(floatArg2fix)
        if abs(x) > 2.**1023:
            y=floatArg1SplitDown*floatArg2SplitDown-((((x*0.5)-(floatArg1SplitUp*0.5)*floatArg2SplitUp)*2.-floatArg1SplitDown*floatArg2SplitUp)-floatArg1SplitUp*floatArg2SplitDown)
        else:
            y=floatArg1SplitDown*floatArg2SplitDown-(((x-floatArg1SplitUp*floatArg2SplitUp)-floatArg1SplitDown*floatArg2SplitUp)-floatArg1SplitUp*floatArg2SplitDown)
        return x,y

    def roundadd(floatArg1,floatArg2,rmode=roundmode.nearest):
        floatArg1=float(floatArg1)
        floatArg2=float(floatArg2)
        x,y=roundfloat.twosum(floatArg1,floatArg2)
        if rmode==roundmode.up:
            if x == float('inf'):
                return x
            elif x == -float('inf'):
                if floatArg1 == -float('inf') or floatArg2 == -float('inf'):
                    return x
                else:
                    return -sys.float_info.max
            if y > 0:
                x=roundfloat.succ(x)
        elif rmode==roundmode.down:
            if x == float('inf'):
                if floatArg1 == float('inf') or floatArg2 == float('inf'):
                    return x
                else:
                    return sys.float_info.max
            elif x == -float('inf'):
                return x
            if y < 0:
                x=roundfloat.pred(x)
        return x

    def roundsub(floatArg1,floatArg2,rmode=roundmode.nearest):
        return roundfloat.roundadd(floatArg1,-floatArg2,rmode)

    def roundmul(floatArg1,floatArg2,rmode=roundmode.nearest):
        floatArg1=float(floatArg1)
        floatArg2=float(floatArg2)
        x,y = roundfloat.twoproduct(floatArg1,floatArg2)
        if rmode == roundmode.up:
            if x == float('inf'):
                return x
            elif x == -float('inf'):
                if abs(floatArg1) == float('inf') or abs(floatArg2) == float('inf'):
                    return x
                else:
                    return -sys.float_info.max
            if abs(x) >= 2.**(-969):
                if y > 0:
                    x=roundfloat.succ(x)
        elif rmode==roundmode.down:
            if x == float('inf'):
                if abs(floatArg1) == float ('inf') or abs(floatArg2) == float ('inf') :
                    return x
                else :
                    return sys.float_info.max
            elif x == -float('inf'):
                return x

            if abs(x) >= 2.**(-969):
                if y < 0.:
                    return roundfloat.pred(x)
            else:
                s1, s2 = roundfloat.twoproduct(floatArg1*2.**537,floatArg2*2.**537)
                t = (x * 2.**537) * 2.**537
                if t > s1 or (t == s1 and s2 < 0.):
                    return roundfloat.pred(x)
        return x

    def rounddiv(floatArg1,floatArg2,rmode=roundmode.nearest):
        floatArg1=float(floatArg1)
        floatArg2=float(floatArg2)
        if rmode==roundmode.up:
            pass
            if floatArg1==0. or floatArg2==0. or abs(floatArg1) == float('inf') or abs(floatArg2) == float('inf') or floatArg1 != floatArg1 or floatArg2 != floatArg2:
                return floatArg1 / floatArg2
            if floatArg2 < 0.:
                floatArg1fix = -floatArg1
                floatArg2fix = -floatArg2
            else:
                floatArg1fix = floatArg1
                floatArg2fix = floatArg2
            if abs(floatArg1fix) < 2.**(-969):
                if abs(floatArg2fix) < 2.**918:
                    floatArg1fix *= 2.**105
                    floatArg2fix *= 2.**105
                else:
                    if floatArg1fix < 0.:
                        return 0.
                    else:
                        return 2.**(-1074)
            d=floatArg1fix / floatArg2fix
            if d==float('inf'):
                return d
            elif d == -float('inf'):
                return -sys.float_info.max

            x,y = roundfloat.twoproduct(d,floatArg2fix)
            if x < floatArg1fix or (x==floatArg1fix and y < 0.):
                return roundfloat.succ(d)
            return d
        elif rmode==roundmode.down:
            if floatArg1 == 0. or floatArg2 == 0. or abs(floatArg1) == float('inf') or abs(floatArg2) == float('inf') or floatArg1 != floatArg1 or floatArg2 != floatArg2:
                return floatArg1 / floatArg2
            if floatArg2 < 0.:
                floatArg1fix = -floatArg1
                floatArg2fix = -floatArg2
            else:
                floatArg1fix = floatArg1
                floatArg2fix = floatArg2

            if abs(floatArg1fix) < 2.**(-969):
                if abs(floatArg2fix) < 2.**918:
                    floatArg1fix *= 2.**105
                    floatArg2fix *= 2.**105
                else:
                    if floatArg1fix < 0.:
                        return -2.**(-1074)
                    else:
                        return 0

            d = floatArg1fix / floatArg2fix
            if d == float('inf'):
                return sys.float_info.max
            elif d == -float('inf'):
                return d
            x,y = roundfloat.twoproduct(d,floatArg2fix)
            if x > floatArg1fix or (x == floatArg1fix and y > 0.):
                return roundfloat.pred(d)
            return d

    def roundsqrt(floatArg,rmode=roundmode.nearest):
        floatArg=float(floatArg)
        d = __math__.sqrt(floatArg)
        if rmode == roundmode.up:
            if floatArg < 2.**(-969):
                a2 = floatArg * 2.**106
                d2 = d * 2.**53
                x,y=roundfloat.twoproduct(d2,d2)
                if x < a2 or (x == a2 and y < 0.):
                    d = roundfloat.succ(d)
            x,y=roundfloat.twoproduct(d,d)
            if x < floatArg or (x==floatArg and y < 0.):
                d=roundfloat.succ(d)

        if rmode == roundmode.down:
            if floatArg < 2.**(-969):
                a2 = floatArg * 2.**106
                d2 = d * 2.**53
                x,y=roundfloat.twoproduct(d2,d2)
                if x > a2 or (x == a2 and y > 0.):
                    d = roundfloat.pred(d)
            x,y=roundfloat.twoproduct(d,d)
            if x > floatArg or (x==floatArg and y > 0.):
                d=roundfloat.pred(d)
        return d