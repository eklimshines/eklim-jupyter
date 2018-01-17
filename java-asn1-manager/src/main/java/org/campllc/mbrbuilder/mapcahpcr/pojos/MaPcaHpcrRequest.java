package org.campllc.mbrbuilder.mapcahpcr.pojos;

public class MaPcaHpcrRequest {
    private String maID;

    public String[] linkageValues;

    public MaPcaHpcrRequest() {
    }

    public String getMaID() { return maID; }

    public void setMaID(String maID) {
        this.maID = maID;
    }

    public String[] getLinkageValues() {
        return linkageValues;
    }

    public void setLinkageValues(String[] linkageValues) {
        this.linkageValues = linkageValues;
    }
}
