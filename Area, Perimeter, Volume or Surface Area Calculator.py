import math

print("\nThis is the Volumne/Area/Perimeter/Surface Area of a Shape Calculator")

unit = input("\nWhat unit are you using (mm, cm, m, km, mi, yds, ft, in) for the measurements?: ")

vora = input("Do you want to calculate an area, perimeter, volume or surface area (of a 3D shape): ")


if vora == "area":
    ashape = input("What shape do you want to calculate the area for (rectangle, triangle, circle, parallelogram, trapezoid, rhombus, kite)?: ")

    if ashape == "rectangle":
        tl = float(input("What is the length?: "))
        tb = float(input("What is the breadth?: "))
        print("\nThe area of the rectangle is:", tl * tb, unit, "squared.")

    elif ashape == "triangle":
        teb = float(input("What is the length of the base?: "))
        teh = float(input("What is the height?: "))
        print("\nThe area of the triangle is:", teb * teh, unit, "squared.")

    elif ashape == "circle":
        cir = float(input("What is the radius (half the diameter)?: "))
        ciarea = 3.14159265359 * (cr**2)
        print("\nThe area of the circle is:", ciarea, unit, "squared")
        cidp = round(carea, 2)
        print("or", cidp, unit, "squared (rounded to 2 decimal places).")

    elif ashape == "parallelogram":
        pb = float(input("What is the length of the base?: "))
        ph = float(input("What is the height?: "))
        print("\nThe area of the parallelogram is:", pb * ph, unit, "squared.")

    elif ashape == "trapezoid":
        tdb = float(input("What is the length of the base?: "))
        tdt = float(input("What is the length of the top?: "))
        tdh = float(input("What is the height?: "))
        print("\nThe area of the trapezoid is:", (tdb + tdt)/2 * tdh, unit, "squared.")

    elif ashape == "rhombus":
        rd1 = float(input("What is the length of the first diagonal?: "))
        rd2 = float(input("What is the length of the second diagonal?: "))
        print("\nThe area of the rhombus is:", (rd1 * rd2)/2, unit, "squared.")

    elif ashape == "kite":
        kd1 = float(input("What is the length of the first diagonal?: "))
        kd2 = float(input("What is the length of the second diagonal?: "))
        print("\nThe area of the kite is:", (kd1 * kd2)/2, unit, "squared.")


elif vora == "volume":
    vshape = input("What shape do you want to calculate the volume for (sphere, cone, pyramid (various), prism (various))?: ")

    if vshape == "sphere":
        sr = float(input("What is the radius (half the diameter)?: "))
        svolume = (4/3) * 3.14159265359  * (sr**3)
        print("\nThe volume of the sphere is:", svolume, unit, "cubed")
        sdp = round(svolume, 2)
        print("or", sdp, unit, "cubed (rounded to 2 decimal places).")

    elif vshape == "cone":
        cor = float(input("What is the radius (half the diameter) of the base?: "))
        coh = float(input("What is the height?: "))
        covolume = (1/3) * 3.14159265359  * (cr**2) * ch
        print("\nThe volume of the cone is:", covolume, unit, "cubed")
        codp = round(cvolume, 2)
        print("or", cdp, unit, "cubed (rounded to 2 decimal places).")

    elif vshape == "pyramid":
        pdshape = input("Which pyramid do you want to calculate the volume for (rectangular based or triangular based)?: ")

        if pdshape == "rectangular based":
            rbpl = float(input("What is the length of the base?: "))
            rbpb = float(input("What is the breadth of the base?: "))
            rbph = float(input("What is the height?: "))
            print("\nThe volume of the rectangular based pyramid is:", (rbpl * rbpb * rbph)/3, unit, "cubed.")

        elif pdshape == "triangular based":
            tbpl = float(input("What is the length of the base?: "))
            tbpb = float(input("What is the height of the base?: "))
            tbph = float(input("What is the height?: "))
            print("\nThe volume of the rectangular based pyramid is:", ((tbpl * tbpb)/2 * tbph)/3, unit, "cubed.")

    elif vshape == "prism":
        pmshape = input("Which prism do you want to calculate the volume for (circular (cylinder), triangular, rectangular (cuboid))?: ")

        if pmshape == "circular":
            cyr = float(input("What is the radius (of the base)?: "))
            cyl = float(input("What is the length?: "))
            cyvolume = 3.14159265359 * (cyr**2) * cyl
            print("\nThe volume of the circular prism (cylinder) is:", cyvolume, unit, "cubed")
            cydp = round(cyvolume, 2)
            print("or", cydp, unit, "cubed (rounded to 2 decimal places).")

        elif pmshape == "triangular":
            trb = float(input("What is the length of the base (of the triangle)?: "))
            trh = float(input("What is the height (of the triangle)?: "))
            trl = float(input("What is the length?: "))
            print("\nThe volume of the triangular prism is:", (trb * trh)/2 * trl, unit, "squared.")

        elif pmshape == "rectangular":
            rcl = float(input("What is the length?: "))
            rcb = float(input("What is the breadth?: "))
            rch = float(input("What is the height?: "))
            print("\nThe volume of the rectangular prism (cuboid) is:", rcl * rcb * rch, unit, "cubed.")


elif vora == "perimeter":
    pshape = input("What (2D) shape do you want to calculate to perimeter for (regular (various), irregular (various) or a circle)?: ")

    if pshape == "regular":
        rel = float(input("What is the length of one side?: "))
        ren = int(input("How many sides are there?: "))
        print("\nThe perimeter of the regular shape is:", rel * ren, unit, ".")

    elif pshape == "irregular":
        ishape = input("What irregular shape do you want to calculate the perimeter of (rectangle, triangle (non-equilateral) or compound (any other shape))?: ")

        if ishape == "rectangle":
            irl = float(input("What is the length?: "))
            irb = float(input("What is the breadth?: "))
            print("\nThe perimeter of the rectangle is:", 2 * irl + 2 * irb, unit, ".")

        elif ishape == "compound":
            number = int(input("How many sides are there (up to 10)?: "))
            if number == 1:
                print("\nWhat's impossible!  Try again.\n")
            elif number == 2:
                print("\nWhat's impossible!  Try again.\n")
            elif number == 3:
                t31 = float(input("What is the length of the first side?: "))
                t32 = float(input("What is the length of the second side?: "))
                t33 = float(input("What is the length of the third side?: "))
                print("\nThe perimeter of the triangle is", t31 + t32 + t33, unit + ".")
            elif number == 4:
                t41 = float(input("What is the length of the first side?: "))
                t42 = float(input("What is the length of the second side?: "))
                t43 = float(input("What is the length of the third side?: "))
                t44 = float(input("What is the length of the fourth side?: "))
                print("\nThe perimeter of the quadrilateral is", t41 + t42 + t43 + t44, unit + ".")
            elif number == 5:
                t51 = float(input("What is the length of the first side?: "))
                t52 = float(input("What is the length of the second side?: "))
                t53 = float(input("What is the length of the third side?: "))
                t54 = float(input("What is the length of the fourth side?: "))
                t55 = float(input("What is the length of the fifth side?: "))
                print("\nThe perimeter of the quadrilateral is", t51 + t52 + t53 + t54 + t55, unit + ".")
            elif number == 6:
                t61 = float(input("What is the length of the first side?: "))
                t62 = float(input("What is the length of the second side?: "))
                t63 = float(input("What is the length of the third side?: "))
                t64 = float(input("What is the length of the fourth side?: "))
                t65 = float(input("What is the length of the fifth side?: "))
                t66 = float(input("What is the length of the sixth side?: "))
                print("\nThe perimeter of the quadrilateral is", t61 + t62 + t63 + t64 + t65 + t66, unit + ".")
            elif number == 7:
                t71 = float(input("What is the length of the first side?: "))
                t72 = float(input("What is the length of the second side?: "))
                t73 = float(input("What is the length of the third side?: "))
                t74 = float(input("What is the length of the fourth side?: "))
                t75 = float(input("What is the length of the fifth side?: "))
                t76 = float(input("What is the length of the sixth side?: "))
                t77 = float(input("What is the length of the seventh side?: "))
                print("\nThe perimeter of the quadrilateral is", t71 + t72 + t73 + t74 + t75 + t76 + t77, unit + ".")
            elif number == 8:
                t81 = float(input("What is the length of the first side?: "))
                t82 = float(input("What is the length of the second side?: "))
                t83 = float(input("What is the length of the third side?: "))
                t84 = float(input("What is the length of the fourth side?: "))
                t85 = float(input("What is the length of the fifth side?: "))
                t86 = float(input("What is the length of the sixth side?: "))
                t87 = float(input("What is the length of the seventh side?: "))
                t88 = float(input("What is the length of the eighth side?: "))
                print("\nThe perimeter of the quadrilateral is", t81 + t82 + t83 + t84 + t85 + t86 + t87 + t88, unit + ".")
            elif number == 9:
                t91 = float(input("What is the length of the first side?: "))
                t92 = float(input("What is the length of the second side?: "))
                t93 = float(input("What is the length of the third side?: "))
                t94 = float(input("What is the length of the fourth side?: "))
                t95 = float(input("What is the length of the fifth side?: "))
                t96 = float(input("What is the length of the sixth side?: "))
                t97 = float(input("What is the length of the seventh side?: "))
                t98 = float(input("What is the length of the eighth side?: "))
                t99 = float(input("What is the length of the ninth side?: "))
                print("\nThe perimeter of the quadrilateral is", t91 + t92 + t93 + t94 + t95 + t96 + t97 + t98 + t99, unit + ".")
            elif number == 10:
                t101 = float(input("What is the length of the first side?: "))
                t102 = float(input("What is the length of the second side?: "))
                t103 = float(input("What is the length of the third side?: "))
                t104 = float(input("What is the length of the fourth side?: "))
                t105 = float(input("What is the length of the fifth side?: "))
                t106 = float(input("What is the length of the sixth side?: "))
                t107 = float(input("What is the length of the seventh side?: "))
                t108 = float(input("What is the length of the eighth side?: "))
                t109 = float(input("What is the length of the ninth side?: "))
                t1010 = float(input("What is the length of the tenth side?: "))
                print("\nThe perimeter of the quadrilateral is", t101 + t102 + t103 + t104 + t105 + t106 + t107 + t108 + t109 + t1010, unit + ".")

        elif ishape == "triangle":
            triangle = input("What type of triangle is it (isosceles, right-angled or scalene)?: ")
            if triangle == "isosceles":
                tis = float(input("What is the length of one of the two equal sides?: "))
                tid = float(input("What is the length of the different side?: "))
                print("\nThe perimeter of the isosceles triangle is", 2 * trs + trd, unit + ".")
            elif triangle == "right-angled":
                tra1 = float(input("What is the length of the first side?: "))
                tra2 = float(input("What is the length of the second side?: "))
                tra3 = float(input("What is the length of the third side?: "))
                print("\nThe perimeter of the right-angled triangle is", tra1 + tra2 + tra3, unit + ".")
            elif triangle == "scalene":
                ts1 = float(input("What is the length of the first side?: "))
                ts2 = float(input("What is the length of the second side?: "))
                ts3 = float(input("What is the length of the third side?: "))
                print("\nThe perimeter of the scalene triangle is", ts1 + ts2 + ts3, unit + ".")

    elif pshape == "circle":
        cer = float(input("What is the radius (half the diameter)?: "))
        cecir = 2 * 3.14159265359 * cer
        print("\nThe perimeter (circumference) of the circle is:", cecir, unit, "squared")
        cedp = round(cecir, 2)
        print("or", cedp, unit, "squared (rounded to 2 decimal places).")


elif vora == "surface area":
    sas = input("What (3D) shape would you like to calculate the surface area of (sphere, cone, pyramid (rectangular), prism (various))?: ")
    if sas == "sphere":
        sasr = float(input("What is the radius (half the diameter)?: "))
        sasa = 4 * 3.14159265359  * (sasr**2)
        print("\nThe surface area of the sphere is:", sasa, unit, "squared")
        sasadp = round(sasa, 2)
        print("or", sasadp, unit, "squared (rounded to 2 decimal places).")
    elif sas == "cone":
        conr = float(input("What is the radius (half the diameter)?: "))
        conh = float(input("What is the height?: "))
        consa = 3.14159265359 * conr * (conr + math.sqrt(conh**2 + conr**2))
        print("\nThe surface area of the cone is", consa, unit, "squared")
        consadp = round(consa, 2)
        print("or", consadp, unit, "squared (rounded to 2 decimal places).")
    elif sas == "pyramid":
        rbpyl = float(input("What is the length of the base?: "))
        rbpyb = float(input("What is the breadth of the base?: "))
        rbpyh = float(input("What is the height?: "))
        rbpysa = rbpyl * rbpyb + rbpyl * math.sqrt((rbpyb / 2)**2 + rbpyh**2) + rbpyb * math.sqrt((rbpyl / 2)**2 + rbpyh**2)
        print("\nThe surface area of the rectangular based pyramid is", rbpysa, unit, "squared")
        rbpysadp = round(rbpysa, 2)
        print("or", rbpysadp, unit, "squared (rounded to 2 decimal places).")
    elif sas == "prism":
        psa = input("What type of prism do you want to calculate the surface area for (circular (cylinder), triangular, rectangular (cuboid))?: ")
        if psa == "circular":
            pcyr = float(input("What is the radius (half the diameter)?: "))
            pcyh = float(input("What is the height?: "))
            pcysa = 2 * 3.14159265359 * pcyr * pcyh + 2 * 3.14159265359 * pcyr**2
            print("\nThe surface area of the circular prism (cylinder) is", pcysa, unit, "squared")
            pcysadp = round(pcysa, 2)
            print("or", pcysadp, unit, "squared rounded to 2 decimal places.")
        elif psa == "triangular":
            tb1 = float(input("What is the length of the first side of the base?: "))
            tb2 = float(input("What is the length of the second side of the base?: "))
            tb3 = float(input("What is the length of the third side of the base?: "))
            tbh = float(input("What is the height?: "))
            tbsa = tb1 * tbh + tb2 * tbh + tb3 * tbh + (1/2) * math.sqrt(- tb1**4 + 2 * (tb1 * tb2)**2 + 2 * (tb1 * tb3)**2 - tb2**4 + 2 * (tb2 * tb3)**2 - tb3**4)
            print("\nThe surface area of the triangular prism is", tbsa, unit, "squared")
            tbsadp = round(tbsa, 2)
            print("or", tbsadp, unit, "squared rounded to 2 decimal places.")


else:
    print("\n[Error]\n**Something you entered was incorrect, please read the instructions carefully and try again.**")

print("\n[Coded, edited and updated by Fin-M]\n")
