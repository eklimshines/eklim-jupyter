package org.campllc.mbrbuilder.maraobeidblacklist.pojos;

public class MaRaObeIdRequest {
    private String maID;
    public String[] rif;

    public void setMaID(String maID){ this.maID = maID;}

    public String getMaID() { return maID; }

    public String[] getRifValues() {
        return rif;
    }

    public void setRifValues(String[] rifValues) {
        this.rif = rifValues;
    }
}
