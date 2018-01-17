package org.campllc.mbrbuilder.objects;

import org.apache.commons.codec.binary.Hex;

/**
 * Created by Griff Baily on 6/19/2017.
 */
public class CommMsg {
    private byte[] msgContent;
    public CommMsg(byte[] msg) {
        msgContent = msg.clone();
    }
    public int getMsgLength() {
        return msgContent.length;
    }
    public byte[] getMsg() {
        return msgContent;
    }
    public String toHex()
    {
        return Hex.encodeHexString(msgContent);
    }
}
