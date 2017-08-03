import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Hashtable;
import java.util.List;

public class Model {
	// even though mz values and retention times should be doubles here
	// everything is a string
	private List<String> mz;
	private int nPathways; // total number of pathways (size of family)
	private Hashtable<String, Integer[]> bounds; // minimum/maximum retention
													// times a cover should have
													// (one per mz)
	private Hashtable<String, Hashtable<String, List<String>>> pathways; // d[mz][color]
																			// --->
																			// {pathway2,...}
	private List<String> pathway_list;

	// private ArrayList<String[]> test1;
	// private ArrayList<String[]> test2;

	public Model() {
		this(test_case_sets(), test_case_limits());
	}

	/*
	 * public Model(ArrayList<String[]> test_case1, ArrayList<String[]>
	 * test_case2){ this.test1 = test_case1; this.test2 = test_case2;
	 * 
	 * }
	 */

	// helper for making f7, f8, ...
	private static void fill(List<String[]> a, String label, int min, int max,
			String color) {
		for (int i = min; i <= max; i++) {
			String[] item = { label, Integer.toString(i), color };
			a.add(item);
		}
	}

	private static Iterable<String[]> test_case_sets() {
		// U = {1...10}, F = { f7 f8 f9 f10 f5 f6 }
		// f7 = {1...7} f8 = {8} f9 = {9} f10 = {10} f5 = {1...5} f6 = {6...10}
		// all same color
		ArrayList<String[]> test = new ArrayList<String[]>();

		fill(test, "f7", 1, 7, "1");
		fill(test, "f8", 8, 8, "1");
		fill(test, "f9", 9, 9, "1");
		fill(test, "f10", 10, 10, "1");
		fill(test, "f5", 1, 5, "2");
		fill(test, "f6", 6, 10, "3");
		fill(test, "f4", 1, 4, "3");
		fill(test, "f2", 5, 6, "2");

		// test case 1
		/*
		 * fill(test,"f1",1,5,"1"); fill(test,"f2",6,10,"2");
		 * fill(test,"f3",6,8,"1"); fill(test,"f4",9,10,"1");
		 */
		// test case2
		/*
		 * fill(test,"f1",1,3,"1"); fill(test,"f2",4,6,"1");
		 * fill(test,"f3",7,9,"2"); fill(test,"f4",10,10,"3");
		 * fill(test,"f5",6,9,"1"); fill(test,"f6",1,9,"2");
		 * fill(test,"f4",10,10,"4");
		 */
		// test case 3 smaller sets but too may colors
		/*
		 * fill(test, "f1", 1, 3, "1"); fill(test, "f2", 4, 4, "1"); //
		 * fill(test,"f2",4,4,"3"); // fill(test,"f2",4,4,"2"); fill(test, "f3",
		 * 5, 9, "1"); fill(test, "f4", 10, 10, "1"); fill(test, "f5", 1, 9,
		 * "2"); fill(test, "f5", 1, 9, "3"); fill(test, "f5", 1, 9, "4");
		 * fill(test, "f5", 1, 9, "5");
		 */
		return test;
	}

	private static Iterable<String[]> test_case_limits() {
		ArrayList<String[]> result = new ArrayList<String[]>();
		for (int n = 1; n <= 10; n++) {
			String[] item = { Integer.toString(n), "1", "1" };// per m/z
			result.add(item);
		}
		return result;
	}

	// input: { [pathway1, mz1,color1], [pathway1, mz2,color5] ... }
	// limits: { [mz1,min,max], [mz2,min,max], ... }
	public Model(Iterable<String[]> input, Iterable<String[]> limits) {
		HashSet<String> universe = new HashSet<String>(); // list of mz values,
															// set for
															// repetition
															// prevention
		HashSet<String> all_pathways = new HashSet<String>(); // list of
																// pathways, set
																// for
																// repetition
																// prevention

		// build "pathways"
		// pathways[mz][color] = {pathway10, pathway1,...}
		Hashtable<String, Hashtable<String, List<String>>> helper = new Hashtable<String, Hashtable<String, List<String>>>();
		for (String[] triple : input) {
			universe.add(triple[1]);
			all_pathways.add(triple[0]);

			Hashtable<String, List<String>> h1 = helper.get(triple[1]);
			if (h1 == null) {
				h1 = new Hashtable<String, List<String>>();
				helper.put(triple[1], h1);
			}
			List<String> h2 = h1.get(triple[2]);
			if (h2 == null) {
				h2 = new ArrayList<String>();
				h1.put(triple[2], h2);
			}
			int pathway_mz_color_index = h2.indexOf(triple[0]);
			if (pathway_mz_color_index == -1) {
				h2.add(triple[0]);
			}
		}

		// populate "bounds"
		bounds = new Hashtable<String, Integer[]>();
		for (String[] b : limits) {
			Integer[] minmax = { Integer.parseInt(b[1]), Integer.parseInt(b[2]) };
			bounds.put(b[0], minmax);
		}
		mz = Arrays.asList(universe.toArray(new String[0]));
		nPathways = mz.size();
		pathways = helper;
		pathway_list = Arrays.asList(all_pathways.toArray(new String[0]));
	}

	public int getPathwayNumber() {
		return nPathways;
	}

	public int getLowerBound(String mz) {
		return bounds.get(mz)[0];
	}

	public int getUpperBound(String mz) {
		return bounds.get(mz)[1];
	}

	public Iterable<String> getMZ() {
		return mz;
	}

	public List<List<String>> getPathways(String mz) {
		List<List<String>> result = new ArrayList<List<String>>();
		Hashtable<String, List<String>> index = pathways.get(mz);
		for (String color : java.util.Collections.list(index.keys())) {
			result.add(index.get(color));
		}
		return result;
	}

	public List<String> getPathways() {
		return pathway_list;
	}
}