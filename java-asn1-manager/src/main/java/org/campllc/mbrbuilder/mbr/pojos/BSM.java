package org.campllc.mbrbuilder.mbr.pojos;

import org.apache.commons.codec.binary.Hex;
import org.campllc.asn1.generated.ieee1609dot2.*;
import org.campllc.asn1.generated.ieee1609dot2basetypes.*;

import java.math.BigInteger;

/**
 * Created by Griff Baily on 6/23/2017.
 */
public class BSM {
    private String timeStamp;
    private String hexMessage;

    public String getTimeStamp() {
        return timeStamp;
    }

    public void setTimeStamp(String timeStamp) {
        this.timeStamp = timeStamp;
    }

    public String getHexMessage() {
        return hexMessage;
    }

    public void setHexMessage(String hexMessage) {
        this.hexMessage = hexMessage;
    }

    private HashedId8 getSigIdent()
    {
        try{
            // TODO
            //return new HashedId8(Hex.decodeHex(digest.toCharArray()));
        }catch(Exception e)
        {
            e.printStackTrace();
        }
        return null;
    }
    private Time64 getExpiryTime()
    {
        /*TODO*/
        return new Time64(new BigInteger("0"));
    }
    private ThreeDLocation getGenLocation()
    {
        /*TODO*/
        return new ThreeDLocation(new Latitude(-900000000),new Longitude(-900000000),new Elevation(0));
    }
    private HashedId3 getP2pcdReq()
    {
        /*TODO*/
        try {
            return new HashedId3(Hex.decodeHex("000000".toCharArray()));
        }catch(Exception e) {
            e.printStackTrace();
        }
        return null;
    }
    private MissingCrlIdentifier getMissingCRLIdent()
    {
        /*TODO*/
        try {
            new MissingCrlIdentifier(new HashedId3(Hex.decodeHex("000000".toCharArray())),new CrlSeries(0));
        }catch(Exception e) {
            e.printStackTrace();
        }
        return null;
    }
    private HashedId3[] getInlineP2pcd()
    {
        /*TODO*/
        try {
            HashedId3[] hashArr={new HashedId3(Hex.decodeHex("000000".toCharArray()))};
            return hashArr;
        }catch(Exception e){
            e.printStackTrace();
        }
        return null;
    }
}
