package org.campllc.mbrbuilder.malalinkageseed.pojos;

public class MaLaLinkageSeedRequest {

    public String maID;

    public String[] lci;

    public String getMaID() { return maID; }

    public void setMaID(String maID) {
        this.maID = maID;
    }

    public String[] getLciValues() {
        return lci;
    }

    public void setLciValues(String[] lci) {
        this.lci = lci;
    }
}
