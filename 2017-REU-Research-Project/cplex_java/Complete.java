import ilog.concert.IloIntExpr;
import ilog.concert.IloIntVar;
import ilog.concert.IloRange;
import ilog.cplex.IloCplex;

import java.util.ArrayList;
import java.util.List;

public class Complete {
	public static void main(String[] args) throws Exception {

		// main code starting here
		IloCplex cplex = new IloCplex();
		Model m = new Model();
		// create array of pathway variables (x)
		List<String> pathwayList = m.getPathways();
		IloIntVar[] x = cplex.boolVarArray(m.getPathwayNumber());

		// add objective
		cplex.addMinimize(cplex.sum(x));

		// create constraints
		// add color number constraints
		for (String mz : m.getMZ()) {
			ArrayList<IloIntVar> colors = new ArrayList<IloIntVar>(); // terms
																		// in ub
																		// >=
																		// c_i1
																		// +
																		// c_i2
																		// ...
																		// >= lb
			// loop iterates once per color assigned to mz value
			for (Iterable<String> pathways : m.getPathways(mz)) {
				IloIntVar c_ij = cplex.boolVar(); // color j selected for mz
													// value i
				colors.add(c_ij);
				ArrayList<IloIntVar> sum_x = new ArrayList<IloIntVar>(); // c_ij
																			// <=
																			// x_k1
																			// +
																			// x_k2
																			// ...
				// iterates once per pathway that assigns color j to mz value i
				for (String p : pathways) {
					// x_k <= c_ij
					int k = pathwayList.indexOf(p);
					cplex.addGe(c_ij, x[k]);
					sum_x.add(x[k]);
				}
				// add upper bound on c_ij
				IloIntExpr sum_x_cplex = cplex.sum(sum_x
						.toArray(new IloIntVar[0]));
				cplex.addLe(c_ij, sum_x_cplex);
			}
			IloIntExpr sum_ci = cplex.sum(colors.toArray(new IloIntVar[0]));
			IloRange colorConstraint = cplex.addRange(m.getLowerBound(mz),
					sum_ci, m.getUpperBound(mz));
		}
		cplex.solve();
		System.out.println("Number of pathways: " + cplex.getObjValue());
		double[] pathways_chosen = cplex.getValues(x);
		System.out.println("Pathways: ");
		for (int i = 0; i < pathways_chosen.length; i++) {
			if (pathways_chosen[i] == 1) {
				System.out.println(pathwayList.get(i));
			}
		}
	}
}
