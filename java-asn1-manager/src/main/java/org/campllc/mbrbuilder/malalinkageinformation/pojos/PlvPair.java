package org.campllc.mbrbuilder.malalinkageinformation.pojos;

public class PlvPair {
        public String laID;
        public int iValue;
        public String reporterPlv;
        public String suspectPlv;

        public String getLaID() {
            return laID;
        }

        public int getIvalue() {
            return iValue;
        }

        public void setIvalue(int ivalue) {
            this.iValue = ivalue;
        }

        public void setLaID(String laID) {
            this.laID = laID;
        }

    public String getReporterPlv() {
        return reporterPlv;
    }

    public String getSuspectPlv() {
        return suspectPlv;
    }
}
