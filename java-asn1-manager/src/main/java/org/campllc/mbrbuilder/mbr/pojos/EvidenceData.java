package org.campllc.mbrbuilder.mbr.pojos;

/**
 * Created by Griff Baily on 6/6/2017.
 * Structure for storing misbehavior reports passed in through the MBRController JSON file.
 * contains lists of VehicleWSMs
 */
public class EvidenceData {
    private VehicleWSMs[] observedNeighborList;
    private VehicleWSMs reporterBSMs;
    private VehicleWSMs[] suspectVehicleList;

    public EvidenceData(){}

    public void setObservedNeighborList(VehicleWSMs[] o)
    {
        observedNeighborList=o;
    }
    public VehicleWSMs[] getObservedNeighborList()
    {
        return observedNeighborList;
    }
    public void setReporterWSMs(VehicleWSMs r)
    {
        reporterBSMs=r;
    }
    public VehicleWSMs getReporterWSMs()
    {
        return reporterBSMs;
    }
    public void setSuspectVehicleList(VehicleWSMs[] s)
    {
        suspectVehicleList=s;
    }
    public VehicleWSMs[] getSuspectVehicleList()
    {
        return suspectVehicleList;
    }

    public String toString()
    {
        return "observedNeighborList:"+"\n"+observedNeighborList+"\n"+"reporterWSMs:"+"\n"+reporterBSMs+"\n"+"suspectVehicleList:"+"\n"+suspectVehicleList;
    }
}
