pro myidlscript

    args=command_line_args()
    inname = args(0)
    outname= args(1)

    mydata= readfits(inname,header)
    mydata= mydata*2

    print, "processing ", inname, " output: ", outname

    writefits, outname, mydata, header
    wait, 10

end
