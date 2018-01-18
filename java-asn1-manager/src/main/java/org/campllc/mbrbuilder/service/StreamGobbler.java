package org.campllc.mbrbuilder.service;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class StreamGobbler implements Runnable {
    InputStream is;
    String type;
    ArrayList<String> output=new ArrayList<String>();

    StreamGobbler(InputStream is, String type)
    {
        this.is = is;
        this.type = type;
    }

    public void run()
    {
        try
        {
            InputStreamReader isr = new InputStreamReader(is);
            BufferedReader br = new BufferedReader(isr);
            String line=null;
            while ( (line = br.readLine()) != null){
                output.add(line);
            }
        } catch (IOException ioe)
        {
            ioe.printStackTrace();
        }
    }
    public String[] getOutput()
    {
        String [] out = output.toArray(new String[output.size()]);
        return out;
    }
}
