package org.campllc.mbrbuilder.maralcirequest.pojos;

public class MaRaLCIRequest {

    private String maID;
    public String[] hpcr;

    public void setMaID(String maID){ this.maID = maID;}

    public String getMaID() { return maID; }

    public String[] getHpcrValues() {
        return hpcr;
    }

    public void setHpcrValues(String[] hpcrValues) {
        this.hpcr = hpcr;
    }

}
