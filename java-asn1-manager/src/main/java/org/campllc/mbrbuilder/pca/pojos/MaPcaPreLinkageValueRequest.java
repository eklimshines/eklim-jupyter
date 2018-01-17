package org.campllc.mbrbuilder.pca.pojos;

/**
 * Created by Shirali Shah on 11/08/2017.
 */

    public class MaPcaPreLinkageValueRequest {

    // Variable declaration
    public String maID;
    public String[] linkageValues;

    public MaPcaPreLinkageValueRequest() {
    }

    public String getMaID() {
        return maID;
    }

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
